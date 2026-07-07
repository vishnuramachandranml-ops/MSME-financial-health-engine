from __future__ import annotations

from pydantic import Field

from app.models.base import AppBaseModel
from app.models.value_objects import MonthlyTimeSeries


class Operations(AppBaseModel):
    """
    Operational business metrics.
    """

    monthly_sales_orders: MonthlyTimeSeries

    monthly_purchase_orders: MonthlyTimeSeries

    vendor_count: int = Field(..., ge=0)

    customer_count: int = Field(..., ge=0)

    repeat_customer_ratio: float | None = Field(
        default=None,
        ge=0,
        le=1,
    )