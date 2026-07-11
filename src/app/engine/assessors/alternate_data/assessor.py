from __future__ import annotations

from app.engine.evaluation.metric_evaluator import MetricEvaluator
from app.engine.models.alternate_data_features import AlternateDataFeatures
from app.engine.models.assessment_result import AssessmentResult
from app.engine.models.component_score import ComponentScore
from app.engine.models.derived_features import DerivedFeatures
from app.engine.scoring.weighted_scorer import WeightedScorer
from app.engine.scorecards.alternate_data_scorecard import (
    GST_FILING_RATE,
    GST_TURNOVER,
    DIGITAL_PAYMENT_RATIO,
    AVERAGE_BANK_BALANCE,
    POSITIVE_BANK_MONTHS,
    ELECTRICITY_STABILITY,
    FUEL_STABILITY,
)


class AlternateDataAssessor:

    COMPONENT_NAME = "Alternate Data"
    COMPONENT_WEIGHT = 0.10
    DEFAULT_CONFIDENCE = 100.0

    def assess(
        self,
        features: AlternateDataFeatures,
    ) -> AssessmentResult:

        metrics = [

            MetricEvaluator.evaluate(
                features.gst_filing_rate,
                GST_FILING_RATE,
            ),

            MetricEvaluator.evaluate(
                features.gst_turnover,
                GST_TURNOVER,
            ),

            MetricEvaluator.evaluate(
                features.digital_payment_ratio,
                DIGITAL_PAYMENT_RATIO,
            ),

            MetricEvaluator.evaluate(
                features.average_bank_balance,
                AVERAGE_BANK_BALANCE,
            ),

            MetricEvaluator.evaluate(
                features.positive_bank_statement_months,
                POSITIVE_BANK_MONTHS,
            ),

            MetricEvaluator.evaluate(
                features.electricity_stability_score,
                ELECTRICITY_STABILITY,
            ),

            MetricEvaluator.evaluate(
                features.fuel_stability_score,
                FUEL_STABILITY,
            ),
        ]

        score = WeightedScorer.calculate(
            [
                (m.score, m.weight)
                for m in metrics
            ]
        )

        return AssessmentResult(
            component=ComponentScore(
                name=self.COMPONENT_NAME,
                score=score,
                weight=self.COMPONENT_WEIGHT,
                confidence=self.DEFAULT_CONFIDENCE,
            ),
            metrics=metrics,
            derived_features=DerivedFeatures(
                values=features.model_dump()
            ),
            positive_signals=self._positive(features),
            negative_signals=self._negative(features),
            warnings=[],
        )

    def _positive(
        self,
        f: AlternateDataFeatures,
    ) -> list[str]:

        signals = []

        if f.gst_filing_rate >= 0.95:
            signals.append(
                "GST filing compliance is excellent."
            )

        if f.digital_payment_ratio >= 0.80:
            signals.append(
                "Business has strong digital payment adoption."
            )

        if f.average_bank_balance >= 1000000:
            signals.append(
                "Business maintains healthy bank balances."
            )

        return signals

    def _negative(
        self,
        f: AlternateDataFeatures,
    ) -> list[str]:

        signals = []

        if f.gst_filing_rate < 0.80:
            signals.append(
                "GST filing consistency needs improvement."
            )

        if f.digital_payment_ratio < 0.50:
            signals.append(
                "Digital payment adoption is relatively low."
            )

        if f.electricity_stability_score < 60:
            signals.append(
                "Electricity usage shows high operational variability."
            )

        return signals