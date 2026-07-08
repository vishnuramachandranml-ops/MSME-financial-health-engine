from __future__ import annotations

from pydantic import Field

from app.models.base import AppBaseModel
from app.models.enums import AssessmentStatus

from app.engine.models.component_score import ComponentScore


class AssessmentSummary(AppBaseModel):
    """
    High-level assessment summary returned to the client.
    """

    financial_health_score: float

    confidence_score: float

    risk_level: str


class AssessmentResponse(AppBaseModel):
    """
    API response returned by the assessment endpoint.
    """

    request_id: str

    status: AssessmentStatus

    summary: AssessmentSummary

    component_scores: list[ComponentScore] = Field(
        default_factory=list
    )

    positive_signals: list[str] = Field(
        default_factory=list
    )

    negative_signals: list[str] = Field(
        default_factory=list
    )

    warnings: list[str] = Field(
        default_factory=list
    )