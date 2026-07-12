from __future__ import annotations

from pydantic import Field

from app.models.base import AppBaseModel


class CashFlowSimulation(AppBaseModel):
    revenue_growth: float | None = None
    operating_margin: float | None = None
    expense_ratio: float | None = None
    collection_days: float | None = None


class FinancialPositionSimulation(AppBaseModel):
    current_ratio: float | None = None
    debt_asset_ratio: float | None = None
    working_capital: float | None = None


class OperationsSimulation(AppBaseModel):
    sales_growth: float | None = None
    capacity_utilization: float | None = None
    operational_efficiency: float | None = None


class ComplianceSimulation(AppBaseModel):
    gst_filing_rate: float | None = None
    epfo_compliance_rate: float | None = None
    tax_delay_days: float | None = None


class AlternateDataSimulation(AppBaseModel):
    digital_payment_ratio: float | None = None
    average_bank_balance: float | None = None


class SimulationInputs(AppBaseModel):

    cashflow: CashFlowSimulation | None = None

    financial_position: FinancialPositionSimulation | None = None

    operations: OperationsSimulation | None = None

    compliance: ComplianceSimulation | None = None

    alternate_data: AlternateDataSimulation | None = None