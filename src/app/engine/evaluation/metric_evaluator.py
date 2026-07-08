from __future__ import annotations

from app.engine.evaluation.metric_result import MetricResult
from app.engine.evaluation.metric_rule import MetricRule
from app.engine.scoring.score_mapper import ScoreMapper


class MetricEvaluator:
    """
    Evaluates a business metric against a configured scoring rule.
    """

    DEFAULT_SCORE = 10.0

    @classmethod
    def evaluate(
        cls,
        value: float,
        rule: MetricRule,
    ) -> MetricResult:
        """
        Evaluate a metric value using the supplied rule.
        """

        if rule.inverse:
            score = ScoreMapper.inverse_threshold(
                value=value,
                thresholds=rule.thresholds,
                default=cls.DEFAULT_SCORE,
            )
        else:
            score = ScoreMapper.threshold(
                value=value,
                thresholds=rule.thresholds,
                default=cls.DEFAULT_SCORE,
            )

        return MetricResult(
            metric=rule.metric,
            value=value,
            score=score,
            weight=rule.weight,
        )