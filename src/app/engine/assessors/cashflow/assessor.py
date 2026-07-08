from __future__ import annotations

from app.engine.evaluation.metric_evaluator import MetricEvaluator
from app.engine.models.assessment_result import AssessmentResult
from app.engine.models.cashflow_features import CashFlowFeatures
from app.engine.models.component_score import ComponentScore
from app.engine.models.derived_features import DerivedFeatures
from app.engine.scoring.weighted_scorer import WeightedScorer
from app.engine.scorecards.cashflow_scorecard import (
    REVENUE_GROWTH,
    NET_CASHFLOW,
    OPERATING_MARGIN,
    EXPENSE_RATIO,
    REVENUE_STABILITY,
    COLLECTION_DAYS,
)


class CashFlowAssessor:

    COMPONENT_NAME = "Cash Flow"
    COMPONENT_WEIGHT = 0.30
    DEFAULT_CONFIDENCE = 100.0

    def assess(
        self,
        features: CashFlowFeatures,
    ) -> AssessmentResult:

        metrics = self._evaluate_metrics(features)

        overall_score = self._calculate_score(metrics)

        return AssessmentResult(
            component=self._build_component_score(overall_score),
            metrics=metrics,
            derived_features=self._build_derived_features(features),
            positive_signals=self._build_positive_signals(features),
            negative_signals=self._build_negative_signals(features),
            warnings=[],
        )

    def _evaluate_metrics(
        self,
        features: CashFlowFeatures,
    ):

        return [

            MetricEvaluator.evaluate(
                features.revenue.growth_rate,
                REVENUE_GROWTH,
            ),

            MetricEvaluator.evaluate(
                features.liquidity.average_net_cashflow,
                NET_CASHFLOW,
            ),

            MetricEvaluator.evaluate(
                features.liquidity.operating_margin * 100,
                OPERATING_MARGIN,
            ),

            MetricEvaluator.evaluate(
                features.cost.expense_ratio * 100,
                EXPENSE_RATIO,
            ),

            MetricEvaluator.evaluate(
                features.revenue.stability_score,
                REVENUE_STABILITY,
            ),

            MetricEvaluator.evaluate(
                features.working_capital.collection_days or 60,
                COLLECTION_DAYS,
            ),
        ]

    def _calculate_score(
        self,
        metrics,
    ) -> float:

        return WeightedScorer.calculate(
            [
                (metric.score, metric.weight)
                for metric in metrics
            ]
        )

    def _build_component_score(
        self,
        score: float,
    ) -> ComponentScore:

        return ComponentScore(
            name=self.COMPONENT_NAME,
            score=score,
            weight=self.COMPONENT_WEIGHT,
            confidence=self.DEFAULT_CONFIDENCE,
        )

    def _build_derived_features(
        self,
        features: CashFlowFeatures,
    ) -> DerivedFeatures:

        return DerivedFeatures(
            values={
                "average_revenue": features.revenue.average,
                "average_expense": features.cost.average,
                "revenue_growth": features.revenue.growth_rate,
                "expense_ratio": features.cost.expense_ratio,
                "operating_margin": features.liquidity.operating_margin,
                "net_cashflow": features.liquidity.average_net_cashflow,
                "stability_score": features.revenue.stability_score,
                "collection_days": features.working_capital.collection_days,
            }
        )

    def _build_positive_signals(
        self,
        features: CashFlowFeatures,
    ) -> list[str]:

        signals = []

        if features.revenue.growth_rate >= 10:
            signals.append(
                "Revenue has shown healthy growth."
            )

        if features.liquidity.operating_margin >= 0.15:
            signals.append(
                "Business maintains a healthy operating margin."
            )

        if features.revenue.stability_score >= 80:
            signals.append(
                "Revenue pattern is stable."
            )

        if features.liquidity.average_net_cashflow > 0:
            signals.append(
                "Business is generating positive cash flow."
            )

        return signals

    def _build_negative_signals(
        self,
        features: CashFlowFeatures,
    ) -> list[str]:

        signals = []

        if features.cost.expense_ratio > 0.80:
            signals.append(
                "Operating expenses are relatively high."
            )

        if (
            features.working_capital.collection_days is not None
            and features.working_capital.collection_days > 90
        ):
            signals.append(
                "Customer collection period is higher than recommended."
            )

        if features.liquidity.average_net_cashflow < 0:
            signals.append(
                "Business is experiencing negative cash flow."
            )

        if features.liquidity.operating_margin < 0:
            signals.append(
                "Business has a negative operating margin."
            )

        return signals