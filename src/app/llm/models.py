from __future__ import annotations

from pydantic import Field

from app.models.base import AppBaseModel


class LLMAnalysis(AppBaseModel):
    executive_summary: str

    credit_opinion: str

    monitoring_points: list[str] = Field(
        default_factory=list,
    )