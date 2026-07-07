from __future__ import annotations

from pydantic import Field

from app.models.base import AppBaseModel
from app.models.enums import AssessmentStatus, RiskLevel


class AssessmentSummary(AppBaseModel):

    financial_health_score: float | None = None

    risk_level: RiskLevel | None = None

    confidence_score: float | None = None


class AssessmentResponse(AppBaseModel):

    request_id: str | None = None

    status: AssessmentStatus

    summary: AssessmentSummary

    positive_signals: list[str] = Field(default_factory=list)

    negative_signals: list[str] = Field(default_factory=list)

    warnings: list[str] = Field(default_factory=list)