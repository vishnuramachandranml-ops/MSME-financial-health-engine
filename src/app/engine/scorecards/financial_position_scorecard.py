from __future__ import annotations

from app.engine.evaluation.metric_rule import MetricRule

# -----------------------------------------------------------------------------
# Financial Position Scorecard
#
# All business rules related to Financial Position scoring are defined here.
# The assessor should never contain thresholds or weights.
# -----------------------------------------------------------------------------

CURRENT_RATIO = MetricRule(
    metric="Current Ratio",
    description="Measures ability to meet short-term obligations.",
    weight=0.20,
    thresholds=[
        (2.0, 100),
        (1.5, 85),
        (1.0, 65),
        (0.8, 40),
    ],
)

DEBT_TO_EQUITY_RATIO = MetricRule(
    metric="Debt to Equity Ratio",
    description="Measures financial leverage relative to net worth.",
    weight=0.20,
    inverse=True,
    thresholds=[
        (1.0, 100),
        (1.5, 80),
        (2.0, 60),
        (3.0, 40),
    ],
)

WORKING_CAPITAL = MetricRule(
    metric="Working Capital",
    description="Measures short-term liquidity buffer.",
    weight=0.15,
    thresholds=[
        (100_000, 100),
        (50_000, 80),
        (0, 60),
        (-50_000, 40),
    ],
)

NET_WORTH = MetricRule(
    metric="Net Worth",
    description="Measures residual business value after liabilities.",
    weight=0.15,
    thresholds=[
        (500_000, 100),
        (250_000, 80),
        (0, 60),
        (-100_000, 30),
    ],
)

ASSET_COVERAGE_RATIO = MetricRule(
    metric="Asset Coverage Ratio",
    description="Measures asset coverage for debt obligations.",
    weight=0.10,
    thresholds=[
        (3.0, 100),
        (2.0, 80),
        (1.5, 60),
        (1.0, 40),
    ],
)

FIXED_ASSET_RATIO = MetricRule(
    metric="Fixed Asset Ratio",
    description="Measures concentration of assets in fixed assets.",
    weight=0.10,
    inverse=True,
    thresholds=[
        (0.40, 100),
        (0.60, 80),
        (0.75, 60),
        (0.90, 40),
    ],
)

DEBT_RATIO = MetricRule(
    metric="Debt Ratio",
    description="Measures liabilities as a share of total assets.",
    weight=0.10,
    inverse=True,
    thresholds=[
        (0.40, 100),
        (0.60, 80),
        (0.75, 60),
        (0.90, 40),
    ],
)

# -----------------------------------------------------------------------------
# Master Scorecard
# -----------------------------------------------------------------------------

FINANCIAL_POSITION_SCORECARD = [
    CURRENT_RATIO,
    DEBT_TO_EQUITY_RATIO,
    WORKING_CAPITAL,
    NET_WORTH,
    ASSET_COVERAGE_RATIO,
    FIXED_ASSET_RATIO,
    DEBT_RATIO,
]
