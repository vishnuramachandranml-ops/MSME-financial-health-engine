from __future__ import annotations

from app.engine.models.alternate_data_features import (
    AlternateDataFeatures,
)
from app.models.alternate_data import AlternateData
from app.utils.math_utils import MathUtils


class AlternateDataCalculator:
    """
    Business calculations for alternate data metrics.
    """

    @staticmethod
    def stability_score(
        values: list[float],
    ) -> float:
        """
        Convert coefficient of variation into a
        0-100 stability score.
        """

        cv = MathUtils.coefficient_of_variation(
            values
        )

        score = 100 * (1 - cv)

        return MathUtils.clamp(
            score,
            0,
            100,
        )

    @classmethod
    def calculate(
        cls,
        alternate_data: AlternateData,
    ) -> AlternateDataFeatures:

        electricity_score = 100.0

        if alternate_data.electricity_units is not None:
            electricity_score = cls.stability_score(
                alternate_data.electricity_units.values
            )

        fuel_score = 100.0

        if alternate_data.fuel_expense is not None:
            fuel_score = cls.stability_score(
                alternate_data.fuel_expense.values
            )

        alternate_score = (
            electricity_score
            + fuel_score
        ) / 2

        return AlternateDataFeatures(
            gst_filing_rate=alternate_data.gst_filing_rate or 0,
            gst_turnover=alternate_data.gst_turnover or 0,
            average_bank_balance=alternate_data.average_bank_balance or 0,
            digital_payment_ratio=alternate_data.digital_payment_ratio or 0,
            positive_bank_statement_months=(
                alternate_data.positive_bank_statement_months
                or 0
            ),
            electricity_stability_score=electricity_score,
            fuel_stability_score=fuel_score,
            alternate_data_score=alternate_score,
        )