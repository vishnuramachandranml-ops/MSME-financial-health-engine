from __future__ import annotations

from pydantic import Field

from app.models.base import AppBaseModel
from app.models.assessment_response import AssessmentResponse


class ComponentDelta(AppBaseModel):
    """
    Comparison of a single assessment component.
    """

    component: str

    before_score: float

    after_score: float

    score_change: float


class ChangedParameter(AppBaseModel):
    """
    Business parameter modified during simulation.
    """

    parameter: str

    before: float | int | None = None

    after: float | int | None = None


class AssessmentDelta(AppBaseModel):
    """
    Overall assessment comparison.
    """

    score_change: float

    previous_risk: str

    new_risk: str

    component_changes: list[ComponentDelta] = Field(
        default_factory=list
    )


class WhatIfResponse(AppBaseModel):
    """
    Response returned by the What-If simulator.
    """

    before: AssessmentResponse

    after: AssessmentResponse

    delta: AssessmentDelta

    changed_parameters: list[ChangedParameter] = Field(
        default_factory=list
    )

    comparison_summary: str | None = None