from __future__ import annotations

from pydantic import Field

from app.models.base import AppBaseModel


class ComponentScore(AppBaseModel):
    """
    Represents the score for a single assessment component.
    """

    name: str = Field(
        ...,
        description="Component name.",
        examples=["Cash Flow"],
    )

    score: float = Field(
        ...,
        ge=0,
        le=100,
        description="Score out of 100.",
    )

    weight: float = Field(
        ...,
        ge=0,
        le=1,
        description="Weight used during aggregation.",
    )

    confidence: float = Field(
        default=100,
        ge=0,
        le=100,
    )