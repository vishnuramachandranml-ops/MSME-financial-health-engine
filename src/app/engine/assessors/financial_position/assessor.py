from __future__ import annotations

from app.engine.evaluation.metric_evaluator import MetricEvaluator
from app.engine.interfaces.base_assessor import BaseAssessor
from app.engine.models.assessment_result import AssessmentResult
from app.engine.models.component_score import ComponentScore
from app.engine.models.derived_features import DerivedFeatures
from app.engine.models.financial_position_features import (
    FinancialPositionFeatures,
)
from app.engine.scoring.weighted_scorer import WeightedScorer
from app.engine.scorecards.financial_position_scorecard import (
    ASSET_COVERAGE_RATIO,
    CURRENT_RATIO,
    DEBT_RATIO,
    DEBT_TO_EQUITY_RATIO,
    FIXED_ASSET_RATIO,
    NET_WORTH,
    WORKING_CAPITAL,
)


class FinancialPositionAssessor(
    BaseAssessor[FinancialPositionFeatures]
):

    COMPONENT_NAME = "Financial Position"
    COMPONENT_WEIGHT = 0.25
    DEFAULT_CONFIDENCE = 100.0

    def assess(
        self,
        features: FinancialPositionFeatures,
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
        features: FinancialPositionFeatures,
    ):

        return [

            MetricEvaluator.evaluate(
                features.current_ratio,
                CURRENT_RATIO,
            ),

            MetricEvaluator.evaluate(
                features.debt_to_equity_ratio,
                DEBT_TO_EQUITY_RATIO,
            ),

            MetricEvaluator.evaluate(
                features.working_capital,
                WORKING_CAPITAL,
            ),

            MetricEvaluator.evaluate(
                features.net_worth,
                NET_WORTH,
            ),

            MetricEvaluator.evaluate(
                features.asset_coverage_ratio,
                ASSET_COVERAGE_RATIO,
            ),

            MetricEvaluator.evaluate(
                features.fixed_asset_ratio,
                FIXED_ASSET_RATIO,
            ),

            MetricEvaluator.evaluate(
                features.debt_ratio,
                DEBT_RATIO,
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
        features: FinancialPositionFeatures,
    ) -> DerivedFeatures:

        return DerivedFeatures(
            values={
                "current_ratio": features.current_ratio,
                "debt_to_equity_ratio": features.debt_to_equity_ratio,
                "working_capital": features.working_capital,
                "net_worth": features.net_worth,
                "asset_coverage_ratio": features.asset_coverage_ratio,
                "fixed_asset_ratio": features.fixed_asset_ratio,
                "debt_ratio": features.debt_ratio,
            }
        )

    def _build_positive_signals(
        self,
        features: FinancialPositionFeatures,
    ) -> list[str]:

        signals = []

        if features.current_ratio >= 1.5:
            signals.append(
                "Business maintains healthy short-term liquidity."
            )

        if features.net_worth > 0:
            signals.append(
                "Business has positive net worth."
            )

        if features.debt_ratio <= 0.60:
            signals.append(
                "Debt levels are within a manageable range."
            )

        if features.working_capital > 0:
            signals.append(
                "Business has positive working capital."
            )

        return signals

    def _build_negative_signals(
        self,
        features: FinancialPositionFeatures,
    ) -> list[str]:

        signals = []

        if features.current_ratio < 1.0:
            signals.append(
                "Current assets may be insufficient to cover "
                "short-term liabilities."
            )

        if features.debt_to_equity_ratio > 2.0:
            signals.append(
                "Debt levels are high relative to net worth."
            )

        if features.net_worth < 0:
            signals.append(
                "Business has negative net worth."
            )

        if features.working_capital < 0:
            signals.append(
                "Business has negative working capital."
            )

        if features.debt_ratio > 0.75:
            signals.append(
                "Liabilities represent a high share of total assets."
            )

        return signals
