from __future__ import annotations

from pydantic import Field

from app.models.base import AppBaseModel


class Compliance(AppBaseModel):
    epfo_registered: bool

    epfo_compliance_rate: float | None = Field(
        default=None,
        ge=0,
        le=1,
    )

    tax_payment_delay_days: int | None = Field(
        default=None,
        ge=0,
    )

    regulatory_notices: int | None = Field(
        default=None,
        ge=0,
    )