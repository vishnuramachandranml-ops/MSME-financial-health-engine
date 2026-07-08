from __future__ import annotations

from app.engine.feature_engineering.financial_position.engineer import (
    FinancialPositionFeatureEngineer,
)
from app.models.financial_position import FinancialPosition


def test_financial_position_engineer_derives_features():
    features = FinancialPositionFeatureEngineer().transform(
        FinancialPosition(
            total_assets=500_000,
            current_assets=200_000,
            fixed_assets=300_000,
            total_liabilities=200_000,
            current_liabilities=100_000,
            long_term_debt=150_000,
        )
    )

    assert features.current_ratio == 2
    assert features.debt_to_equity_ratio == 250_000 / 300_000
    assert features.working_capital == 100_000
    assert features.net_worth == 300_000
    assert features.asset_coverage_ratio == 2
    assert features.fixed_asset_ratio == 0.6
    assert features.debt_ratio == 0.4


def test_financial_position_engineer_uses_supplied_net_worth_and_working_capital():
    features = FinancialPositionFeatureEngineer().transform(
        FinancialPosition(
            total_assets=500_000,
            current_assets=200_000,
            fixed_assets=300_000,
            total_liabilities=200_000,
            current_liabilities=100_000,
            long_term_debt=150_000,
            net_worth=350_000,
            working_capital=125_000,
        )
    )

    assert features.net_worth == 350_000
    assert features.working_capital == 125_000
