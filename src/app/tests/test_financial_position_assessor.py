from __future__ import annotations

from app.engine.assessors.financial_position.assessor import (
    FinancialPositionAssessor,
)
from app.engine.models.financial_position_features import FinancialPositionFeatures


def test_financial_position_assessor_returns_assessment_result():
    result = FinancialPositionAssessor().assess(
        FinancialPositionFeatures(
            current_ratio=2.0,
            debt_to_equity_ratio=0.8,
            working_capital=150_000,
            net_worth=500_000,
            asset_coverage_ratio=3.0,
            fixed_asset_ratio=0.5,
            debt_ratio=0.4,
        )
    )

    assert result.component.name == "Financial Position"
    assert result.component.score == 98
    assert len(result.metrics) == 7
    assert result.derived_features.values["current_ratio"] == 2.0
    assert result.positive_signals
    assert not result.negative_signals
