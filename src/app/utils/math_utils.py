from __future__ import annotations

from statistics import mean, stdev


class MathUtils:
    """Reusable mathematical helper functions."""

    EPSILON = 1e-9

    @staticmethod
    def safe_divide(
        numerator: float,
        denominator: float,
        default: float = 0.0,
    ) -> float:
        """Safely divide two numbers."""
        if abs(denominator) < MathUtils.EPSILON:
            return default
        return numerator / denominator

    @staticmethod
    def average(values: list[float]) -> float:
        """Calculate arithmetic mean."""
        return mean(values)

    @staticmethod
    def percentage_change(
        old: float,
        new: float,
    ) -> float:
        """Percentage change between two values."""
        return MathUtils.safe_divide(
            new - old,
            old,
        ) * 100

    @staticmethod
    def coefficient_of_variation(
        values: list[float],
    ) -> float:
        """
        Standard deviation divided by mean.
        Lower is more stable.
        """
        if len(values) < 2:
            return 0.0

        avg = mean(values)

        if abs(avg) < MathUtils.EPSILON:
            return 0.0

        return stdev(values) / avg

    @staticmethod
    def clamp(
        value: float,
        minimum: float,
        maximum: float,
    ) -> float:
        return max(minimum, min(maximum, value))