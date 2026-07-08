from __future__ import annotations

from app.utils.math_utils import MathUtils


class ComplianceCalculator:
    """
    Performs compliance score calculations.
    """

    @staticmethod
    def calculate_gst_score(
        is_registered: bool,
        filing_rate: float,
    ) -> float:
        if not is_registered:
            return 0.0

        return MathUtils.clamp(
            filing_rate * 100,
            0,
            100,
        )

    @staticmethod
    def calculate_epfo_score(
        is_registered: bool,
        compliance_rate: float,
    ) -> float:
        if not is_registered:
            return 100.0

        return MathUtils.clamp(
            compliance_rate * 100,
            0,
            100,
        )

    @staticmethod
    def calculate_tax_delay_score(
        delay_days: int,
    ) -> float:
        score = 100 - (delay_days * 2)

        return MathUtils.clamp(
            score,
            0,
            100,
        )

    @staticmethod
    def calculate_regulatory_score(
        regulatory_notices: int,
    ) -> float:
        score = 100 - (regulatory_notices * 25)

        return MathUtils.clamp(
            score,
            0,
            100,
        )

    @staticmethod
    def calculate_statutory_score(
        statutory_dues_pending: bool,
    ) -> float:
        if statutory_dues_pending:
            return 40.0

        return 100.0

    @staticmethod
    def calculate_overall_compliance(
        scores: list[float],
    ) -> float:
        return MathUtils.average(scores)
