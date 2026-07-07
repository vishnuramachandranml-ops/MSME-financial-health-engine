from __future__ import annotations

from pydantic import Field, model_validator

from app.models.base import AppBaseModel
from app.models.value_objects import MonthlyTimeSeries


class CashFlow(AppBaseModel):
    """
    Cash flow related information.
    """

    monthly_revenue: MonthlyTimeSeries

    monthly_expenses: MonthlyTimeSeries

    average_collection_days: int | None = Field(
        default=None,
        ge=0,
        le=365,
    )

    average_supplier_payment_days: int | None = Field(
        default=None,
        ge=0,
        le=365,
    )

    @model_validator(mode="after")
    def validate_lengths(self):
        if len(self.monthly_revenue.values) != len(self.monthly_expenses.values):
            raise ValueError(
                "Revenue and expense history must have equal length."
            )
        return self