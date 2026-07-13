from __future__ import annotations

from enum import Enum


class CreditDecision(str, Enum):
    APPROVE = "APPROVE"
    CONDITIONAL_APPROVAL = "CONDITIONAL APPROVAL"
    REVIEW = "REVIEW"
    REJECT = "REJECT"