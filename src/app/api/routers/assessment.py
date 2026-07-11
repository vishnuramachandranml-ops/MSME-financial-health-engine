from __future__ import annotations

from fastapi import APIRouter

from app.models.assessment_request import AssessmentRequest
from app.models.assessment_response import (
    AssessmentResponse,
    AssessmentSummary,
)

from app.engine.recommendations.recommendation_engine import (
    RecommendationEngine,
)
from app.models.enums import AssessmentStatus
from app.pipelines.assessment_pipeline import AssessmentPipeline
from app.engine.risk.risk_classifier import RiskClassifier
from app.llm.summary_service import SummaryService

router = APIRouter(
    prefix="/assessment",
    tags=["Assessment"],
)

# Create once at application startup
pipeline = AssessmentPipeline()

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

    return AssessmentResponse(
        request_id=request.metadata.request_id,
        status=AssessmentStatus.SUCCESS,
        summary=summary,
        component_scores=result.component_scores,
        positive_signals=result.positive_signals,
        negative_signals=result.negative_signals,
        recommendations=recommendations,
        llm_analysis=llm_analysis,
        warnings=result.warnings,
    )
