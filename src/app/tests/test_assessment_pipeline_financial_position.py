from __future__ import annotations

from app.models.assessment_request import AssessmentRequest
from app.models.business_profile import BusinessProfile
from app.models.financial_position import FinancialPosition
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
