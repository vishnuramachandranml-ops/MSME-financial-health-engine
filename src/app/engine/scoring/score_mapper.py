from __future__ import annotations

from typing import Iterable


class ScoreMapper:
    """
    Maps metric values to normalized scores using threshold rules.
    """

    @staticmethod
    def threshold(
        value: float,
        thresholds: Iterable[tuple[float, float]],
        default: float = 0.0,
    ) -> float:
        """
        Higher value is better.

        Example:
        thresholds=[
            (20,100),
            (10,85),
            (0,70),
            (-10,40)
        ]
        """
        for threshold, score in thresholds:
            if value >= threshold:
                return score

        return default

    @staticmethod
    def inverse_threshold(
        value: float,
        thresholds: Iterable[tuple[float, float]],
        default: float = 0.0,
    ) -> float:
        """
        Lower value is better.

        Example:
        thresholds=[
            (50,100),
            (70,80),
            (85,60),
            (100,40)
        ]
        """
        for threshold, score in thresholds:
            if value <= threshold:
                return score

        return default