from __future__ import annotations

from pydantic import Field

from app.models.base import AppBaseModel
from app.models.value_objects import MonthlyTimeSeries


class AlternateData(AppBaseModel):
    gst_registered: bool

    gst_filing_rate: float | None = Field(default=None, ge=0, le=1)

    gst_turnover: float | None = Field(default=None, ge=0)

    upi_transaction_count: int | None = Field(default=None, ge=0)

    upi_transaction_volume: float | None = Field(default=None, ge=0)

    electricity_units: MonthlyTimeSeries | None = None

    fuel_expense: MonthlyTimeSeries | None = None