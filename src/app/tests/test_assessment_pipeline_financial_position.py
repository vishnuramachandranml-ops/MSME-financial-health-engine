from __future__ import annotations

from app.models.assessment_request import AssessmentRequest
from app.models.business_profile import BusinessProfile
from app.models.cashflow import CashFlow
from app.models.financial_position import FinancialPosition
from app.models.value_objects import MonthlyTimeSeries
from app.pipelines.assessment_pipeline import AssessmentPipeline


def test_assessment_pipeline_invokes_financial_position_assessment():
    request = AssessmentRequest(
        business_profile=BusinessProfile(
            business_id="MSME001",
            business_name="Example MSME",
            business_type="Private Limited",
            business_age_years=5,
            employee_count=25,
            annual_turnover=2_000_000,
            location="Bengaluru",
        ),
        financial_position=FinancialPosition(
            total_assets=500_000,
            current_assets=200_000,
            fixed_assets=300_000,
            total_liabilities=200_000,
            current_liabilities=100_000,
            long_term_debt=150_000,
        ),
    )

    result = AssessmentPipeline().assess(request)

    assert result.component.name == "Financial Position"
    assert result.derived_features.values["current_ratio"] == 2


def test_assessment_pipeline_keeps_cashflow_when_financial_position_exists():
    request = AssessmentRequest(
        business_profile=BusinessProfile(
            business_id="MSME001",
            business_name="Example MSME",
            business_type="Private Limited",
            business_age_years=5,
            employee_count=25,
            annual_turnover=2_000_000,
            location="Bengaluru",
        ),
        cashflow=CashFlow(
            monthly_revenue=MonthlyTimeSeries(
                values=[
                    100_000,
                    110_000,
                    120_000,
                    130_000,
                    140_000,
                    150_000,
                ]
            ),
            monthly_expenses=MonthlyTimeSeries(
                values=[
                    80_000,
                    85_000,
                    90_000,
                    95_000,
                    100_000,
                    105_000,
                ]
            ),
            average_collection_days=45,
        ),
        financial_position=FinancialPosition(
            total_assets=500_000,
            current_assets=200_000,
            fixed_assets=300_000,
            total_liabilities=200_000,
            current_liabilities=100_000,
            long_term_debt=150_000,
        ),
    )

    result = AssessmentPipeline().assess(request)

    assert result.component.name == "Overall"
    assert [
        component.name
        for component in result.component_scores
    ] == [
        "Cash Flow",
        "Financial Position",
    ]
    assert "revenue_growth" in result.derived_features.values
    assert "current_ratio" in result.derived_features.values
