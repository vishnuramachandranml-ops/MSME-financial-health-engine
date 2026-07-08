from app.engine.interfaces.base_feature_engineer import BaseFeatureEngineer
from app.engine.feature_engineering.cashflow.calculator import CashFlowCalculator
from app.engine.models.cashflow_features import (
    CashFlowFeatures,
    RevenueMetrics,
    CostMetrics,
    LiquidityMetrics,
    WorkingCapitalMetrics,
)
from app.models.cashflow import CashFlow


class CashFlowFeatureEngineer(
    BaseFeatureEngineer[CashFlow, CashFlowFeatures]
):
    """
    Converts CashFlow input into engine-ready features.
    """

    def transform(
        self,
        data: CashFlow,
    ) -> CashFlowFeatures:

        revenue = data.monthly_revenue.values
        expense = data.monthly_expenses.values

        avg_revenue = CashFlowCalculator.average(revenue)
        avg_expense = CashFlowCalculator.average(expense)

        avg_net_cashflow = CashFlowCalculator.average_net_cashflow(
            revenue,
            expense,
        )

        return CashFlowFeatures(
            revenue=RevenueMetrics(
                average=avg_revenue,
                growth_rate=CashFlowCalculator.revenue_growth(revenue),
                stability_score=CashFlowCalculator.stability_score(revenue),
            ),
            cost=CostMetrics(
                average=avg_expense,
                expense_ratio=CashFlowCalculator.expense_ratio(
                    avg_expense,
                    avg_revenue,
                ),
            ),
            liquidity=LiquidityMetrics(
                average_net_cashflow=avg_net_cashflow,
                operating_margin=CashFlowCalculator.operating_margin(
                    avg_net_cashflow,
                    avg_revenue,
                ),
            ),
            working_capital=WorkingCapitalMetrics(
                collection_days=data.average_collection_days,
                supplier_payment_days=data.average_supplier_payment_days,
            ),
        )