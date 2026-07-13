from __future__ import annotations

from app.models.credit_decision import CreditDecision
from app.models.monitoring_frequency import MonitoringFrequency


class DecisionEngine:

    @staticmethod
    def credit_decision(score: float) -> CreditDecision:

        if score >= 80:
            return CreditDecision.APPROVE

        if score >= 65:
            return CreditDecision.CONDITIONAL_APPROVAL

        if score >= 50:
            return CreditDecision.REVIEW

        return CreditDecision.REJECT

    @staticmethod
    def suggested_loan_amount(
        score: float,
        requested_amount: float,
    ) -> float:

        if score >= 85:
            factor = 1.00

        elif score >= 75:
            factor = 0.90

        elif score >= 65:
            factor = 0.80

        elif score >= 50:
            factor = 0.60

        else:
            factor = 0.00

        return round(requested_amount * factor, 2)

    @staticmethod
    def loan_limit_range(
        suggested_amount: float,
    ) -> tuple[float, float]:

        lower = round(suggested_amount * 0.90, 2)
        upper = round(suggested_amount * 1.10, 2)

        return lower, upper

    @staticmethod
    def monitoring_frequency(
        score: float,
    ) -> MonitoringFrequency:

        if score >= 85:
            return MonitoringFrequency.YEARLY

        if score >= 75:
            return MonitoringFrequency.HALF_YEARLY

        if score >= 60:
            return MonitoringFrequency.QUARTERLY

        return MonitoringFrequency.MONTHLY

    @staticmethod
    def risk_grade(
        score: float,
    ) -> str:

        if score >= 95:
            return "AAA"

        if score >= 90:
            return "AA+"

        if score >= 85:
            return "AA"

        if score >= 80:
            return "A+"

        if score >= 75:
            return "A"

        if score >= 70:
            return "BBB"

        if score >= 65:
            return "BB+"

        if score >= 60:
            return "BB"

        if score >= 50:
            return "B+"

        if score >= 40:
            return "B"

        return "C"