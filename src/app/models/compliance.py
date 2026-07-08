from __future__ import annotations

from pydantic import Field

from app.models.base import AppBaseModel


class Compliance(AppBaseModel):
    """
    Business regulatory compliance information.
    """

    gst_registered: bool = True

    gst_return_filing_rate: float | None = Field(
        default=None,
        ge=0,
        le=1,
    )

    itr_filed_last_3_years: bool = True

    epfo_registered: bool = True

    epfo_compliance_rate: float | None = Field(
        default=None,
        ge=0,
        le=1,
    )

    tax_payment_delay_days: int | None = Field(
        default=None,
        ge=0,
    )

    statutory_dues_pending: bool = False

    regulatory_notices: int | None = Field(
        default=None,
        ge=0,
    )