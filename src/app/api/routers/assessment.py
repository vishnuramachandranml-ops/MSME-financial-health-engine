from __future__ import annotations

from fastapi import APIRouter

from app.models.assessment_request import AssessmentRequest
from app.models.assessment_response import (
    AssessmentResponse,
    AssessmentSummary,
)
from app.models.enums import AssessmentStatus
from app.pipelines.assessment_pipeline import AssessmentPipeline

router = APIRouter(
    prefix="/assessment",
    tags=["Assessment"],
)

# Create once at application startup
pipeline = AssessmentPipeline()

print(AssessmentResponse.model_fields.keys())
@router.post(
    "",
    response_model=AssessmentResponse,
)
async def assess(
    request: AssessmentRequest,
) -> AssessmentResponse:
    """
    Perform financial health assessment for an MSME.
    """

    result = pipeline.assess(request)

    summary = AssessmentSummary(
        financial_health_score=result.component.score,
        confidence_score=result.component.confidence,
        risk_level="LOW",  # TODO: Replace with RiskAssessment module later
    )

    return AssessmentResponse(
        request_id=request.metadata.request_id,
        status=AssessmentStatus.SUCCESS,
        summary=summary,
        component_scores=[
            result.component,
        ],
        positive_signals=result.positive_signals,
        negative_signals=result.negative_signals,
        warnings=result.warnings,
    )