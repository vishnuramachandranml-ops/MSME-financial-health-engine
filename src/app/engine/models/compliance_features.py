from __future__ import annotations

from pydantic import Field

from app.models.base import AppBaseModel


class ComplianceFeatures(AppBaseModel):
    """
    Derived compliance features used for assessment.
    """

    gst_compliance_score: float = Field(..., ge=0, le=100)

    epfo_compliance_score: float = Field(..., ge=0, le=100)

    tax_payment_score: float = Field(..., ge=0, le=100)

    regulatory_score: float = Field(..., ge=0, le=100)

    statutory_score: float = Field(..., ge=0, le=100)

    overall_compliance_rate: float = Field(..., ge=0, le=100)

    gst_return_filing_rate: float = Field(..., ge=0, le=1)

    epfo_compliance_rate: float = Field(..., ge=0, le=1)

    tax_payment_delay_days: int = Field(..., ge=0)

    regulatory_notices: int = Field(..., ge=0)

    statutory_dues_pending: bool
