from __future__ import annotations

from app.engine.feature_engineering.financial_position.calculator import (
    FinancialPositionCalculator,
)


def test_financial_position_calculator_derives_balance_sheet_metrics():
    assert FinancialPositionCalculator.current_ratio(200_000, 100_000) == 2
    assert FinancialPositionCalculator.debt_to_equity_ratio(150_000, 300_000) == 0.5
    assert FinancialPositionCalculator.working_capital(200_000, 100_000) == 100_000
    assert FinancialPositionCalculator.net_worth(500_000, 200_000) == 300_000
    assert FinancialPositionCalculator.asset_coverage_ratio(500_000, 250_000) == 2
    assert FinancialPositionCalculator.fixed_asset_ratio(300_000, 500_000) == 0.6
    assert FinancialPositionCalculator.debt_ratio(200_000, 500_000) == 0.4
