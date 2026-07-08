from __future__ import annotations

from app.utils.math_utils import MathUtils


class CashFlowCalculator:
    """Business calculations for cash flow metrics."""

    @staticmethod
    def average(values: list[float]) -> float:
        return MathUtils.average(values)

    @staticmethod
    def average_net_cashflow(
        revenue: list[float],
        expense: list[float],
    ) -> float:
        net = [
            r - e
            for r, e in zip(revenue, expense, strict=True)
        ]
        return MathUtils.average(net)

    @staticmethod
    def revenue_growth(
        revenue: list[float],
    ) -> float:
        return MathUtils.percentage_change(
            revenue[0],
            revenue[-1],
        )

    @staticmethod
    def expense_ratio(
        average_expense: float,
        average_revenue: float,
    ) -> float:
        return MathUtils.safe_divide(
            average_expense,
            average_revenue,
        )

    @staticmethod
    def operating_margin(
        average_net_cashflow: float,
        average_revenue: float,
    ) -> float:
        return MathUtils.safe_divide(
            average_net_cashflow,
            average_revenue,
        )

    @staticmethod
    def stability_score(
        revenue: list[float],
    ) -> float:
        """
        Convert coefficient of variation into
        a 0–100 stability score.

        Higher = more stable.
        """
        cv = MathUtils.coefficient_of_variation(
            revenue
        )

        score = 100 * (1 - cv)

        return MathUtils.clamp(
            score,
            0,
            100,
        )