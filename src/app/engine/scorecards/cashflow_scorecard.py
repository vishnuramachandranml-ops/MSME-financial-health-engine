from __future__ import annotations

from app.engine.evaluation.metric_rule import MetricRule

# -----------------------------------------------------------------------------
# Cash Flow Scorecard
#
# All business rules related to Cash Flow scoring are defined here.
# The assessor should never contain thresholds or weights.
# -----------------------------------------------------------------------------

REVENUE_GROWTH = MetricRule(
    metric="Revenue Growth",
    description="Measures revenue growth over the last six months.",
    weight=0.25,
    thresholds=[
        (20, 100),
        (10, 85),
        (0, 70),
        (-10, 40),
    ],
)

NET_CASHFLOW = MetricRule(
    metric="Net Cash Flow",
    description="Measures average monthly net cash flow.",
    weight=0.25,
    thresholds=[
        (0, 100),
        (-50_000, 60),
    ],
)

OPERATING_MARGIN = MetricRule(
    metric="Operating Margin",
    description="Measures operating profitability.",
    weight=0.20,
    thresholds=[
        (20, 100),
        (10, 80),
        (5, 60),
        (0, 40),
    ],
)

EXPENSE_RATIO = MetricRule(
    metric="Expense Ratio",
    description="Lower operating expenses are better.",
    weight=0.15,
    inverse=True,
    thresholds=[
        (50, 100),
        (70, 80),
        (85, 60),
        (100, 40),
    ],
)

REVENUE_STABILITY = MetricRule(
    metric="Revenue Stability",
    description="Measures consistency of monthly revenue.",
    weight=0.10,
    thresholds=[
        (90, 100),
        (75, 80),
        (60, 60),
        (40, 40),
    ],
)

COLLECTION_DAYS = MetricRule(
    metric="Collection Days",
    description="Measures customer payment efficiency.",
    weight=0.05,
    inverse=True,
    thresholds=[
        (30, 100),
        (60, 80),
        (90, 60),
        (120, 40),
    ],
)

# -----------------------------------------------------------------------------
# Master Scorecard
# -----------------------------------------------------------------------------

CASHFLOW_SCORECARD = [
    REVENUE_GROWTH,
    NET_CASHFLOW,
    OPERATING_MARGIN,
    EXPENSE_RATIO,
    REVENUE_STABILITY,
    COLLECTION_DAYS,
]