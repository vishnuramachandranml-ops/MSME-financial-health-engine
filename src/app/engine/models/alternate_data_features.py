from __future__ import annotations

from pydantic import Field

from app.models.base import AppBaseModel


class AlternateDataFeatures(AppBaseModel):
    """
    Derived alternate-data features used for assessment.
    """

    gst_filing_rate: float = Field(..., ge=0, le=1)

    gst_turnover: float = Field(..., ge=0)

    average_bank_balance: float = Field(..., ge=0)

    digital_payment_ratio: float = Field(..., ge=0, le=1)

    positive_bank_statement_months: int = Field(..., ge=0, le=12)

    electricity_stability_score: float = Field(..., ge=0, le=100)

    fuel_stability_score: float = Field(..., ge=0, le=100)

    alternate_data_score: float = Field(..., ge=0, le=100)