from __future__ import annotations

from pydantic import Field

from app.models.base import AppBaseModel


class DerivedFeatures(AppBaseModel):
    """
    Stores calculated business metrics.

    Flexible enough for all assessors.
    """

    values: dict[str, float] = Field(
        default_factory=dict
    )