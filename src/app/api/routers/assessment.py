from __future__ import annotations

from app.models.assessment_request import AssessmentRequest
from app.models.assessment_response import (
    AssessmentResponse,
    AssessmentSummary,
)

from app.engine.recommendations.recommendation_engine import (
    RecommendationEngine,
)
from app.models.component_breakdown import (
    ComponentBreakdown,
    MetricBreakdown,
)
from app.models.enums import AssessmentStatus
from app.pipelines.assessment_pipeline import AssessmentPipeline
from app.engine.risk.risk_classifier import RiskClassifier
from app.llm.summary_service import SummaryService
from fastapi import APIRouter, Body

from app.models.simulation_inputs import (
    SimulationInputs,
    CashFlowSimulation,
    FinancialPositionSimulation,
    OperationsSimulation,
    ComplianceSimulation,
    AlternateDataSimulation,
)

from app.examples.swagger_examples import (
    HEALTHY_MANUFACTURING,
    MEDIUM_RISK_MANUFACTURING,
    NEW_TO_CREDIT,
    HIGH_RISK_MANUFACTURING,
)

router = APIRouter(
    prefix="/assessment",
    tags=["FinancialAssessment"],
)

# Create once at application startup
pipeline = AssessmentPipeline()

@router.post(
    "",
    response_model=AssessmentResponse,
    summary="Assess MSME Financial Health",
    description="""
Performs an explainable financial health assessment for an MSME.

Evaluates:
• Cash Flow
• Financial Position
• Compliance
• Operations
• Alternate Data

Returns:
• Financial Health Score
• Risk Classification
• AI Executive Summary
• Recommendations
• Component Breakdown
""",
    responses={
        200: {
            "description": "Assessment completed successfully"
        },
        400: {
            "description": "Invalid assessment request"
        },
        500: {
            "description": "Internal server error"
        },
    },
)
async def assess(
    request: AssessmentRequest = Body(
        ...,
            openapi_examples={
        "healthy": {
            "summary": "Healthy Manufacturing MSME",
            "description": "Excellent financial health.",
            "value": HEALTHY_MANUFACTURING,
        },
        "medium": {
            "summary": "Medium Risk Manufacturing MSME",
            "description": "Moderate liquidity concerns.",
            "value": MEDIUM_RISK_MANUFACTURING,
        },
        "new_to_credit": {
            "summary": "New-to-Credit MSME",
            "description": "Limited credit history with strong alternate data.",
            "value": NEW_TO_CREDIT,
        },
        "high": {
            "summary": "High Risk Manufacturing MSME",
            "description": "Weak financial position.",
            "value": HIGH_RISK_MANUFACTURING,
        },
        },
    ),
):
    """
    Perform financial health assessment for an MSME.
    """

    result = pipeline.assess(request)
    risk_level = RiskClassifier.classify(
        result.component.score
    )

    
    recommendations = RecommendationEngine.generate(
        result
    )

    llm_analysis = SummaryService().summarize(
        result=result,
        risk_level=risk_level.value,
        recommendations=recommendations,
    )

    summary = AssessmentSummary(
        financial_health_score=result.component.score,
        risk_level=risk_level,
        confidence_score=result.component.confidence,
    )

    component_breakdown = []

    for assessment in result.component_assessments:

        component_breakdown.append(

            ComponentBreakdown(

                component=assessment.component.name,

                score=assessment.component.score,

                confidence=assessment.component.confidence,

                metrics=[

                    MetricBreakdown(

                        metric=metric.metric,

                        value=metric.value,

                        score=metric.score,

                        weight=metric.weight,

                    )

                    for metric in assessment.metrics

                ],

                positive_signals=assessment.positive_signals,

                negative_signals=assessment.negative_signals,

            )

        )

    derived = result.derived_features.values

    simulation_inputs = SimulationInputs(

        cashflow=CashFlowSimulation(
            revenue_growth=derived.get("revenue_growth"),
            operating_margin=derived.get("operating_margin") * 100 if derived.get("operating_margin") is not None else None,
            expense_ratio=derived.get("expense_ratio") * 100 if derived.get("expense_ratio") is not None else None,
            collection_days=derived.get("collection_days"),
        ),

        financial_position=FinancialPositionSimulation(
            current_ratio=derived.get("current_ratio"),
            debt_asset_ratio=derived.get("debt_ratio") * 100 if derived.get("debt_ratio") is not None else None,
            working_capital=derived.get("working_capital"),
        ),

        operations=OperationsSimulation(
            sales_growth=derived.get("sales_growth"),
            capacity_utilization=derived.get("capacity_utilization") * 100 if derived.get("capacity_utilization") is not None else None,
            operational_efficiency=derived.get("operational_efficiency_score"),
        ),

        compliance=ComplianceSimulation(
            gst_filing_rate=derived.get("gst_filing_rate") * 100 if derived.get("gst_filing_rate") is not None else None,
            epfo_compliance_rate=derived.get("epfo_compliance_rate") * 100 if derived.get("epfo_compliance_rate") is not None else None,
            tax_delay_days=derived.get("tax_payment_delay_days"),
        ),

        alternate_data=AlternateDataSimulation(
            digital_payment_ratio=derived.get("digital_payment_ratio") * 100 if derived.get("digital_payment_ratio") is not None else None,
            average_bank_balance=derived.get("average_bank_balance"),                    # See note below
        ),
    )

    return AssessmentResponse(
        request_id=request.metadata.request_id,
        status=AssessmentStatus.SUCCESS,
        summary=summary,
        component_scores=result.component_scores,
        component_breakdown=component_breakdown,
        positive_signals=result.positive_signals,
        negative_signals=result.negative_signals,
        recommendations=recommendations,
        simulation_inputs=simulation_inputs,
        llm_analysis=llm_analysis,
        warnings=result.warnings,
    )
