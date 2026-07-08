from __future__ import annotations

from app.engine.evaluation.metric_rule import MetricRule

# -----------------------------------------------------------------------------
# Compliance Scorecard
#
# All business rules related to Compliance scoring are defined here.
# The assessor should never contain thresholds or weights.
# -----------------------------------------------------------------------------

GST_RETURN_FILING = MetricRule(
    metric="GST Return Filing",
    description="Measures GST return filing consistency.",
    weight=0.20,
    thresholds=[
        (95, 100),
        (90, 85),
        (80, 65),
        (70, 40),
    ],
)

EPFO_COMPLIANCE = MetricRule(
    metric="EPFO Compliance",
    description="Measures EPFO statutory compliance.",
    weight=0.15,
    thresholds=[
        (95, 100),
        (90, 85),
        (80, 65),
        (70, 40),
    ],
)

TAX_PAYMENT = MetricRule(
    metric="Tax Payment",
    description="Measures tax payment timeliness.",
    weight=0.20,
    thresholds=[
        (95, 100),
        (80, 85),
        (60, 65),
        (40, 40),
    ],
)

REGULATORY_NOTICES = MetricRule(
    metric="Regulatory Notices",
    description="Measures regulatory notice burden.",
    weight=0.15,
    thresholds=[
        (100, 100),
        (75, 80),
        (50, 60),
        (25, 40),
    ],
)

STATUTORY_DUES = MetricRule(
    metric="Statutory Dues",
    description="Measures pending statutory dues risk.",
    weight=0.15,
    thresholds=[
        (100, 100),
        (80, 80),
        (60, 60),
        (40, 40),
    ],
)

OVERALL_COMPLIANCE = MetricRule(
    metric="Overall Compliance",
    description="Measures combined regulatory and statutory compliance.",
    weight=0.15,
    thresholds=[
        (90, 100),
        (80, 85),
        (70, 65),
        (60, 40),
    ],
)

# -----------------------------------------------------------------------------
# Master Scorecard
# -----------------------------------------------------------------------------

COMPLIANCE_SCORECARD = [
    GST_RETURN_FILING,
    EPFO_COMPLIANCE,
    TAX_PAYMENT,
    REGULATORY_NOTICES,
    STATUTORY_DUES,
    OVERALL_COMPLIANCE,
]
