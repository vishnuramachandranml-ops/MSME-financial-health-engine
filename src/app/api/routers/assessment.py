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
from app.api.response_builder import (
    build_assessment_response,
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
    return build_assessment_response(
        request=request,
        result=result,
    )