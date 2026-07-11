from __future__ import annotations

from app.engine.risk.constants import (
    LOW_RISK_THRESHOLD,
    MEDIUM_RISK_THRESHOLD,
    HIGH_RISK_THRESHOLD,
)
from app.models.enums import RiskLevel


class RiskClassifier:
    """
    Converts the financial health score into a lending risk category.
    """

    @staticmethod
    def classify(score: float) -> RiskLevel:

        if score >= LOW_RISK_THRESHOLD:
            return RiskLevel.LOW

        if score >= MEDIUM_RISK_THRESHOLD:
            return RiskLevel.MEDIUM

        if score >= HIGH_RISK_THRESHOLD:
            return RiskLevel.HIGH

        return RiskLevel.VERY_HIGH