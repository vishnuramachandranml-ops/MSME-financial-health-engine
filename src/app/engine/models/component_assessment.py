from __future__ import annotations

from pydantic import Field

from app.models.base import AppBaseModel

from app.engine.evaluation.metric_result import MetricResult
from app.engine.models.component_score import ComponentScore


class ComponentAssessment(AppBaseModel):
    """
    Detailed assessment for a single component.
    """

    component: ComponentScore

    metrics: list[MetricResult] = Field(
        default_factory=list,
    )

    positive_signals: list[str] = Field(
        default_factory=list,
    )

    negative_signals: list[str] = Field(
        default_factory=list,
    )

    warnings: list[str] = Field(
        default_factory=list,
    )