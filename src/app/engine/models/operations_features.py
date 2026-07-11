from __future__ import annotations

from pydantic import Field

from app.models.base import AppBaseModel


class OperationsFeatures(AppBaseModel):
    """
    Derived operational features used for assessment.
    """

    sales_growth: float = Field(
        ...,
        description="Sales growth percentage.",
    )

    purchase_growth: float = Field(
        ...,
        description="Purchase growth percentage.",
    )

    repeat_customer_ratio: float = Field(
        ...,
        ge=0,
        le=1,
    )

    vendor_diversification_score: float = Field(
        ...,
        ge=0,
        le=100,
    )

    customer_diversification_score: float = Field(
        ...,
        ge=0,
        le=100,
    )

    capacity_utilization: float = Field(
        ...,
        ge=0,
        le=1,
    )

    inventory_turnover: float = Field(
        ...,
        ge=0,
    )

    order_fulfillment_rate: float = Field(
        ...,
        ge=0,
        le=1,
    )

    employee_productivity: float = Field(
        ...,
        ge=0,
    )

    operational_efficiency_score: float = Field(
        ...,
        ge=0,
        le=100,
    )

    monthly_sales_average: float = Field(
        ...,
        ge=0,
    )

    monthly_purchase_average: float = Field(
        ...,
        ge=0,
    )