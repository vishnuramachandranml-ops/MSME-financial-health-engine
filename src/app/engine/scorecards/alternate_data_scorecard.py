from __future__ import annotations

from app.engine.evaluation.metric_rule import MetricRule

GST_FILING_RATE = MetricRule(
    metric="GST Filing Rate",
    description="GST filing consistency.",
    weight=0.20,
    thresholds=[
        (0.95, 100),
        (0.90, 85),
        (0.80, 65),
        (0.70, 40),
    ],
)

GST_TURNOVER = MetricRule(
    metric="GST Turnover",
    description="Business turnover from GST.",
    weight=0.15,
    thresholds=[
        (10000000, 100),
        (5000000, 85),
        (2000000, 65),
        (500000, 40),
    ],
)

DIGITAL_PAYMENT_RATIO = MetricRule(
    metric="Digital Payment Ratio",
    description="Digital payment adoption.",
    weight=0.15,
    thresholds=[
        (0.90, 100),
        (0.75, 85),
        (0.60, 65),
        (0.40, 40),
    ],
)

AVERAGE_BANK_BALANCE = MetricRule(
    metric="Average Bank Balance",
    description="Average operating bank balance.",
    weight=0.15,
    thresholds=[
        (2000000, 100),
        (1000000, 85),
        (500000, 65),
        (100000, 40),
    ],
)

POSITIVE_BANK_MONTHS = MetricRule(
    metric="Positive Bank Months",
    description="Months with positive bank balance.",
    weight=0.10,
    thresholds=[
        (12, 100),
        (10, 85),
        (8, 65),
        (6, 40),
    ],
)

ELECTRICITY_STABILITY = MetricRule(
    metric="Electricity Stability",
    description="Operational stability based on electricity consumption.",
    weight=0.15,
    thresholds=[
        (90, 100),
        (80, 85),
        (70, 65),
        (60, 40),
    ],
)

FUEL_STABILITY = MetricRule(
    metric="Fuel Stability",
    description="Operational stability based on fuel consumption.",
    weight=0.10,
    thresholds=[
        (90, 100),
        (80, 85),
        (70, 65),
        (60, 40),
    ],
)

ALTERNATE_DATA_SCORECARD = [
    GST_FILING_RATE,
    GST_TURNOVER,
    DIGITAL_PAYMENT_RATIO,
    AVERAGE_BANK_BALANCE,
    POSITIVE_BANK_MONTHS,
    ELECTRICITY_STABILITY,
    FUEL_STABILITY,
]