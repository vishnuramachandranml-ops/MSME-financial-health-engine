from __future__ import annotations

from copy import deepcopy

from app.models.assessment_request import AssessmentRequest
from app.models.simulation_inputs import (
    AlternateDataSimulation,
    CashFlowSimulation,
    ComplianceSimulation,
    FinancialPositionSimulation,
    OperationsSimulation,
    SimulationInputs,
)


class WhatIfService:

    def apply(
        self,
        request: AssessmentRequest,
        scenario: SimulationInputs,
    ) -> AssessmentRequest:

        modified = deepcopy(request)

        self._apply_cashflow(
            modified,
            scenario.cashflow,
        )

        self._apply_financial_position(
            modified,
            scenario.financial_position,
        )

        self._apply_operations(
            modified,
            scenario.operations,
        )

        self._apply_compliance(
            modified,
            scenario.compliance,
        )

        self._apply_alternate_data(
            modified,
            scenario.alternate_data,
        )

        return modified

    def _apply_cashflow(
        self,
        request: AssessmentRequest,
        scenario: CashFlowSimulation | None,
    ) -> None:

        if (
            scenario is None
            or request.cashflow is None
        ):
            return

        revenue = request.cashflow.monthly_revenue.values
        expenses = request.cashflow.monthly_expenses.values

        # -------------------------------
        # Revenue Growth
        # -------------------------------
        if scenario.revenue_growth is not None:

            revenue = self._generate_revenue_series(
                first_value=revenue[0],
                target_growth=scenario.revenue_growth,
                periods=len(revenue),
            )

            request.cashflow.monthly_revenue.values = revenue

        # -------------------------------
        # Operating Margin takes precedence
        # over Expense Ratio
        # -------------------------------
        if scenario.operating_margin is not None:

            expenses = self._generate_expense_from_margin(
                revenue,
                scenario.operating_margin,
            )

            request.cashflow.monthly_expenses.values = expenses

        elif scenario.expense_ratio is not None:

            expenses = self._generate_expense_from_ratio(
                revenue,
                scenario.expense_ratio,
            )

            request.cashflow.monthly_expenses.values = expenses

        # -------------------------------
        # Collection Days
        # -------------------------------
        if scenario.collection_days is not None:

            request.cashflow.average_collection_days = (
                scenario.collection_days
            )

    def _generate_revenue_series(
        self,
        first_value: float,
        target_growth: float,
        periods: int,
    ) -> list[float]:

        if periods <= 1:
            return [round(first_value, 2)]

        last_value = first_value * (
            1 + target_growth / 100
        )

        increment = (
            last_value - first_value
        ) / (periods - 1)

        return [
            round(
                first_value + increment * i,
                2,
            )
            for i in range(periods)
        ]

    def _generate_expense_from_ratio(
        self,
        revenue: list[float],
        expense_ratio: float,
    ) -> list[float]:

        ratio = expense_ratio / 100

        return [
            round(r * ratio, 2)
            for r in revenue
        ]

    def _generate_expense_from_margin(
    self,
        revenue: list[float],
        margin: float,
    ) -> list[float]:

        margin = margin / 100

        return [
            round(
                r * (1 - margin),
                2,
            )
            for r in revenue
        ]

    def _apply_financial_position(
        self,
        request: AssessmentRequest,
        scenario: FinancialPositionSimulation | None,
    ) -> None:

        if (
            scenario is None
            or request.financial_position is None
        ):
            return

        fp = request.financial_position

        # Working Capital takes precedence
        if scenario.working_capital is not None:

            fp.working_capital = scenario.working_capital

            fp.current_assets = (
                fp.current_liabilities
                + scenario.working_capital
            )

        elif scenario.current_ratio is not None:

            fp.current_assets = (
                scenario.current_ratio
                * fp.current_liabilities
            )

            fp.working_capital = (
                fp.current_assets
                - fp.current_liabilities
            )

        if scenario.debt_asset_ratio is not None:

            fp.total_liabilities = (
                fp.total_assets
                * scenario.debt_asset_ratio
                / 100
            )

            fp.net_worth = (
                fp.total_assets
                - fp.total_liabilities
            )
            
    def _apply_operations(
        self,
        request: AssessmentRequest,
        scenario: OperationsSimulation | None,
    ) -> None:

        if (
            scenario is None
            or request.operations is None
        ):
            return

        operations = request.operations

        # ------------------------------------
        # Capacity Utilization (%)
        # UI sends 0-100
        # Model expects 0-1
        # ------------------------------------
        if scenario.capacity_utilization is not None:

            operations.capacity_utilization = (
                scenario.capacity_utilization / 100
            )
        # ------------------------------------
        # Sales Growth (%)
        # ------------------------------------
        if scenario.sales_growth is not None:

            operations.monthly_sales_orders.values = (
                self._generate_revenue_series(
                    first_value=operations.monthly_sales_orders.values[0],
                    target_growth=scenario.sales_growth,
                    periods=len(
                        operations.monthly_sales_orders.values
                    ),
                )
            )
    def _apply_compliance(
        self,
        request: AssessmentRequest,
        scenario: ComplianceSimulation | None,
    ) -> None:

        if (
            scenario is None
            or request.compliance is None
        ):
            return

        compliance = request.compliance

        # ------------------------------------
        # GST Filing Rate (%)
        # UI : 0-100
        # Model : 0-1
        # ------------------------------------
        if scenario.gst_filing_rate is not None:

            compliance.gst_return_filing_rate = (
                scenario.gst_filing_rate / 100
            )

        # ------------------------------------
        # EPFO Compliance Rate (%)
        # UI : 0-100
        # Model : 0-1
        # ------------------------------------
        if scenario.epfo_compliance_rate is not None:

            compliance.epfo_compliance_rate = (
                scenario.epfo_compliance_rate / 100
            )

        # ------------------------------------
        # Tax Payment Delay (Days)
        # ------------------------------------
        if scenario.tax_delay_days is not None:

            compliance.tax_payment_delay_days = (
                scenario.tax_delay_days
            )

    def _apply_alternate_data(
        self,
        request: AssessmentRequest,
        scenario: AlternateDataSimulation | None,
    ) -> None:

        if (
            scenario is None
            or request.alternate_data is None
        ):
            return

        alternate_data = request.alternate_data

        # ------------------------------------
        # Digital Payment Ratio (%)
        # UI : 0-100
        # Model : 0-1
        # ------------------------------------
        if scenario.digital_payment_ratio is not None:

            alternate_data.digital_payment_ratio = (
                scenario.digital_payment_ratio / 100
            )

        # ------------------------------------
        # Average Bank Balance
        # ------------------------------------
        if scenario.average_bank_balance is not None:

            alternate_data.average_bank_balance = (
                scenario.average_bank_balance
            )