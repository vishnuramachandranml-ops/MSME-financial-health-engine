from __future__ import annotations

from pydantic import Field

from app.models.base import AppBaseModel


class RevenueMetrics(AppBaseModel):
    average: float = Field(..., ge=0)
    growth_rate: float
    stability_score: float = Field(..., ge=0, le=100)


class CostMetrics(AppBaseModel):
    average: float = Field(..., ge=0)
    expense_ratio: float = Field(..., ge=0)


class LiquidityMetrics(AppBaseModel):
    average_net_cashflow: float
    operating_margin: float


class WorkingCapitalMetrics(AppBaseModel):
    collection_days: int | None = None
    supplier_payment_days: int | None = None


class CashFlowFeatures(AppBaseModel):
    revenue: RevenueMetrics
    cost: CostMetrics
    liquidity: LiquidityMetrics
    working_capital: WorkingCapitalMetrics