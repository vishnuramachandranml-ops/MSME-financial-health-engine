from __future__ import annotations

from app.utils.math_utils import MathUtils


class FinancialPositionCalculator:
    """
    Performs financial ratio calculations.
    """

    @staticmethod
    def current_ratio(
        current_assets: float,
        current_liabilities: float,
    ) -> float:
        return MathUtils.safe_divide(
            current_assets,
            current_liabilities,
        )

    @staticmethod
    def debt_to_equity_ratio(
        total_debt: float,
        net_worth: float,
    ) -> float:
        return MathUtils.safe_divide(
            total_debt,
            net_worth,
        )

    @staticmethod
    def working_capital(
        current_assets: float,
        current_liabilities: float,
    ) -> float:
        return current_assets - current_liabilities

    @staticmethod
    def net_worth(
        total_assets: float,
        total_liabilities: float,
    ) -> float:
        return total_assets - total_liabilities

    @staticmethod
    def asset_coverage_ratio(
        total_assets: float,
        total_debt: float,
    ) -> float:
        return MathUtils.safe_divide(
            total_assets,
            total_debt,
        )

    @staticmethod
    def fixed_asset_ratio(
        fixed_assets: float,
        total_assets: float,
    ) -> float:
        return MathUtils.safe_divide(
            fixed_assets,
            total_assets,
        )

    @staticmethod
    def debt_ratio(
        total_liabilities: float,
        total_assets: float,
    ) -> float:
        return MathUtils.safe_divide(
            total_liabilities,
            total_assets,
        )