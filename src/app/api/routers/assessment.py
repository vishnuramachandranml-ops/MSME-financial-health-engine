from fastapi import APIRouter

from app.models.assessment_request import AssessmentRequest
from app.models.assessment_response import (
    AssessmentResponse,
    AssessmentSummary,
)
from app.models.enums import AssessmentStatus

router = APIRouter(tags=["Assessment"])


@router.post(
    "/assessment",
    response_model=AssessmentResponse,
)
async def assess(
    request: AssessmentRequest,
):

    return AssessmentResponse(
        request_id=request.metadata.request_id,
        status=AssessmentStatus.SUCCESS,
        summary=AssessmentSummary(),
        warnings=[
            "Financial Health Engine is under development."
        ],
    )