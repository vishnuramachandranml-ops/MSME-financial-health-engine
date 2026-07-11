from __future__ import annotations

# Sales Growth (%)
SALES_GROWTH_THRESHOLDS = [
    (20, 100),
    (10, 85),
    (0, 70),
    (-10, 40),
]

# Purchase Growth (%)
PURCHASE_GROWTH_THRESHOLDS = [
    (20, 100),
    (10, 85),
    (0, 70),
    (-10, 40),
]

# Repeat Customer Ratio
REPEAT_CUSTOMER_THRESHOLDS = [
    (0.80, 100),
    (0.60, 85),
    (0.40, 70),
    (0.20, 40),
]

# Capacity Utilization
CAPACITY_UTILIZATION_THRESHOLDS = [
    (0.90, 100),
    (0.75, 85),
    (0.60, 70),
    (0.40, 40),
]

# Inventory Turnover
INVENTORY_TURNOVER_THRESHOLDS = [
    (12, 100),
    (8, 85),
    (5, 70),
    (2, 40),
]

# Order Fulfillment
ORDER_FULFILLMENT_THRESHOLDS = [
    (0.98, 100),
    (0.95, 85),
    (0.90, 70),
    (0.80, 40),
]

# Employee Productivity
EMPLOYEE_PRODUCTIVITY_THRESHOLDS = [
    (1000000, 100),
    (750000, 85),
    (500000, 70),
    (250000, 40),
]