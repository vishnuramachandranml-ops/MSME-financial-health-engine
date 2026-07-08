from __future__ import annotations

from pydantic import Field

from app.models.base import AppBaseModel

from app.engine.evaluation.metric_result import MetricResult
from app.engine.models.component_score import ComponentScore
from app.engine.models.derived_features import DerivedFeatures


class AssessmentResult(AppBaseModel):
    """
    Internal engine output produced by an assessor.

    This model is consumed by the assessment pipeline and later
    transformed into an API response.
    """

    component: ComponentScore

    metrics: list[MetricResult] = Field(
        default_factory=list,
        description="Detailed metric-wise scoring results.",
    )

    derived_features: DerivedFeatures = Field(
        default_factory=DerivedFeatures,
        description="Derived business features used during assessment.",
    )

    positive_signals: list[str] = Field(
        default_factory=list,
        description="Positive observations identified during assessment.",
    )

    negative_signals: list[str] = Field(
        default_factory=list,
        description="Negative observations identified during assessment.",
    )

    warnings: list[str] = Field(
        default_factory=list,
        description="Warnings generated during assessment.",
    )