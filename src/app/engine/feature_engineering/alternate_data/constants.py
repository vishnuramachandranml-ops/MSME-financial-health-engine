from __future__ import annotations

# GST Filing Rate
GST_FILING_RATE_THRESHOLDS = [
    (0.95, 100),
    (0.90, 85),
    (0.80, 65),
    (0.70, 40),
]

# GST Turnover (INR)
GST_TURNOVER_THRESHOLDS = [
    (10_000_000, 100),
    (5_000_000, 85),
    (2_000_000, 65),
    (500_000, 40),
]

# Average Bank Balance (INR)
AVERAGE_BANK_BALANCE_THRESHOLDS = [
    (2_000_000, 100),
    (1_000_000, 85),
    (500_000, 65),
    (100_000, 40),
]

# Digital Payment Ratio
DIGITAL_PAYMENT_RATIO_THRESHOLDS = [
    (0.90, 100),
    (0.75, 85),
    (0.60, 65),
    (0.40, 40),
]

# Positive Bank Statement Months
POSITIVE_BANK_MONTHS_THRESHOLDS = [
    (12, 100),
    (10, 85),
    (8, 65),
    (6, 40),
]

# Stability Score
STABILITY_SCORE_THRESHOLDS = [
    (90, 100),
    (80, 85),
    (70, 65),
    (60, 40),
]