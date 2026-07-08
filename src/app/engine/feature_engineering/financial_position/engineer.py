from app.engine.feature_engineering.financial_position.calculator import (
    FinancialPositionCalculator,
)
from app.engine.feature_engineering.financial_position.constants import (
    DEFAULT_AMOUNT,
)
from app.engine.interfaces.base_feature_engineer import BaseFeatureEngineer
from app.engine.models.financial_position_features import (
    FinancialPositionFeatures,
)
from app.models.financial_position import FinancialPosition


class FinancialPositionFeatureEngineer(
    BaseFeatureEngineer[FinancialPosition, FinancialPositionFeatures]
):
    """
    Converts FinancialPosition input into engine-ready features.
    """

    def transform(
        self,
        data: FinancialPosition,
    ) -> FinancialPositionFeatures:

        total_assets = self._amount(data.total_assets)
        current_assets = self._amount(data.current_assets)
        fixed_assets = self._amount(data.fixed_assets)
        total_liabilities = self._amount(data.total_liabilities)
        current_liabilities = self._amount(data.current_liabilities)
        long_term_debt = self._amount(data.long_term_debt)

        total_debt = current_liabilities + long_term_debt

        net_worth = data.net_worth
        if net_worth is None:
            net_worth = FinancialPositionCalculator.net_worth(
                total_assets,
                total_liabilities,
            )

        working_capital = data.working_capital
        if working_capital is None:
            working_capital = FinancialPositionCalculator.working_capital(
                current_assets,
                current_liabilities,
            )

        return FinancialPositionFeatures(
            current_ratio=FinancialPositionCalculator.current_ratio(
                current_assets,
                current_liabilities,
            ),
            debt_to_equity_ratio=FinancialPositionCalculator.debt_to_equity_ratio(
                total_debt,
                net_worth,
            ),
            working_capital=working_capital,
            net_worth=net_worth,
            asset_coverage_ratio=FinancialPositionCalculator.asset_coverage_ratio(
                total_assets,
                total_debt,
            ),
            fixed_asset_ratio=FinancialPositionCalculator.fixed_asset_ratio(
                fixed_assets,
                total_assets,
            ),
            debt_ratio=FinancialPositionCalculator.debt_ratio(
                total_liabilities,
                total_assets,
            ),
        )

    def _amount(
        self,
        value: float | None,
    ) -> float:

        return value if value is not None else DEFAULT_AMOUNT
