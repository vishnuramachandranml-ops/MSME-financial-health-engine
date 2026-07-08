from __future__ import annotations

from app.engine.assessors.cashflow.assessor import CashFlowAssessor
from app.engine.assessors.financial_position.assessor import (
    FinancialPositionAssessor,
)
from app.engine.feature_engineering.cashflow.engineer import CashFlowFeatureEngineer
from app.engine.feature_engineering.financial_position.engineer import (
    FinancialPositionFeatureEngineer,
)
from app.engine.models.assessment_result import AssessmentResult
from app.engine.models.component_score import ComponentScore
from app.engine.models.derived_features import DerivedFeatures
from app.engine.scoring.weighted_scorer import WeightedScorer
from app.models.assessment_request import AssessmentRequest


class AssessmentPipeline:
    """
    Orchestrates the financial assessment workflow.
    """

    def __init__(self) -> None:
        self._cashflow_engineer = CashFlowFeatureEngineer()
        self._cashflow_assessor = CashFlowAssessor()
        self._financial_position_engineer = FinancialPositionFeatureEngineer()
        self._financial_position_assessor = FinancialPositionAssessor()

    def assess(
        self,
        request: AssessmentRequest,
    ) -> AssessmentResult:
        """
        Execute the assessment pipeline.
        """

        results = []

        if request.cashflow is not None:
            cashflow_features = self._cashflow_engineer.transform(
                request.cashflow
            )

            results.append(
                self._cashflow_assessor.assess(
                    cashflow_features
                )
            )

        if request.financial_position is not None:
            financial_position_features = self._financial_position_engineer.transform(
                request.financial_position
            )

            results.append(
                self._financial_position_assessor.assess(
                    financial_position_features
                )
            )

        if len(results) == 1:
            return results[0]

        return self._aggregate_results(results)

    def _aggregate_results(
        self,
        results: list[AssessmentResult],
    ) -> AssessmentResult:

        component_scores = [
            result.component
            for result in results
        ]

        overall_score = WeightedScorer.calculate(
            [
                (component.score, component.weight)
                for component in component_scores
            ]
        )

        overall_confidence = WeightedScorer.calculate(
            [
                (component.confidence, component.weight)
                for component in component_scores
            ]
        )

        return AssessmentResult(
            component=ComponentScore(
                name="Overall",
                score=overall_score,
                weight=sum(
                    component.weight
                    for component in component_scores
                ),
                confidence=overall_confidence,
            ),
            component_scores=component_scores,
            metrics=[
                metric
                for result in results
                for metric in result.metrics
            ],
            derived_features=DerivedFeatures(
                values={
                    key: value
                    for result in results
                    for key, value in result.derived_features.values.items()
                }
            ),
            positive_signals=[
                signal
                for result in results
                for signal in result.positive_signals
            ],
            negative_signals=[
                signal
                for result in results
                for signal in result.negative_signals
            ],
            warnings=[
                warning
                for result in results
                for warning in result.warnings
            ],
        )
