from __future__ import annotations


class WeightedScorer:
    """
    Calculates weighted average score.
    """

    @staticmethod
    def calculate(
        scores: list[tuple[float, float]],
    ) -> float:
        """
        scores = [
            (metric_score, weight),
            ...
        ]
        """

        total_weight = sum(weight for _, weight in scores)

        if total_weight == 0:
            return 0.0

        weighted_sum = sum(
            score * weight
            for score, weight in scores
        )

        return round(weighted_sum / total_weight, 2)