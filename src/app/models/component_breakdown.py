from __future__ import annotations

from pydantic import Field

from app.models.base import AppBaseModel


class MetricBreakdown(AppBaseModel):
    metric: str

    value: float

    score: float

    weight: float


class ComponentBreakdown(AppBaseModel):
    component: str

    score: float

    confidence: float

    metrics: list[MetricBreakdown] = Field(
        default_factory=list,
    )

    positive_signals: list[str] = Field(
        default_factory=list,
    )

    negative_signals: list[str] = Field(
        default_factory=list,
    )