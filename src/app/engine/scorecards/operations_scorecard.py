from __future__ import annotations

from app.engine.evaluation.metric_rule import MetricRule

# -----------------------------------------------------------------------------
# Operations Scorecard
#
# All business rules related to Operations scoring are defined here.
# -----------------------------------------------------------------------------

SALES_GROWTH = MetricRule(
    metric="Sales Growth",
    description="Measures sales growth trend.",
    weight=0.20,
    thresholds=[
        (20, 100),
        (10, 85),
        (0, 65),
        (-10, 40),
    ],
)

PURCHASE_GROWTH = MetricRule(
    metric="Purchase Growth",
    description="Measures purchase growth trend.",
    weight=0.10,
    thresholds=[
        (20, 100),
        (10, 85),
        (0, 65),
        (-10, 40),
    ],
)

REPEAT_CUSTOMERS = MetricRule(
    metric="Repeat Customers",
    description="Measures customer retention.",
    weight=0.15,
    thresholds=[
        (0.80, 100),
        (0.60, 85),
        (0.40, 65),
        (0.20, 40),
    ],
)

VENDOR_DIVERSIFICATION = MetricRule(
    metric="Vendor Diversification",
    description="Measures supplier diversification.",
    weight=0.10,
    thresholds=[
        (90, 100),
        (75, 85),
        (60, 65),
        (40, 40),
    ],
)

CUSTOMER_DIVERSIFICATION = MetricRule(
    metric="Customer Diversification",
    description="Measures customer concentration risk.",
    weight=0.10,
    thresholds=[
        (90, 100),
        (75, 85),
        (60, 65),
        (40, 40),
    ],
)

CAPACITY_UTILIZATION = MetricRule(
    metric="Capacity Utilization",
    description="Measures production utilization.",
    weight=0.10,
    thresholds=[
        (0.90, 100),
        (0.75, 85),
        (0.60, 65),
        (0.40, 40),
    ],
)

ORDER_FULFILLMENT = MetricRule(
    metric="Order Fulfillment",
    description="Measures operational reliability.",
    weight=0.10,
    thresholds=[
        (0.98, 100),
        (0.95, 85),
        (0.90, 65),
        (0.80, 40),
    ],
)

OPERATIONAL_EFFICIENCY = MetricRule(
    metric="Operational Efficiency",
    description="Overall operational efficiency score.",
    weight=0.15,
    thresholds=[
        (90, 100),
        (80, 85),
        (70, 65),
        (60, 40),
    ],
)

OPERATIONS_SCORECARD = [
    SALES_GROWTH,
    PURCHASE_GROWTH,
    REPEAT_CUSTOMERS,
    VENDOR_DIVERSIFICATION,
    CUSTOMER_DIVERSIFICATION,
    CAPACITY_UTILIZATION,
    ORDER_FULFILLMENT,
    OPERATIONAL_EFFICIENCY,
]