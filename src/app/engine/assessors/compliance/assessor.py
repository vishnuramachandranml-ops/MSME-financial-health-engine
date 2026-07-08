from __future__ import annotations

from app.engine.evaluation.metric_evaluator import MetricEvaluator
from app.engine.interfaces.base_assessor import BaseAssessor
from app.engine.models.assessment_result import AssessmentResult
from app.engine.models.compliance_features import ComplianceFeatures
from app.engine.models.component_score import ComponentScore
from app.engine.models.derived_features import DerivedFeatures
from app.engine.scoring.weighted_scorer import WeightedScorer
from app.engine.scorecards.compliance_scorecard import (
    EPFO_COMPLIANCE,
    GST_RETURN_FILING,
    OVERALL_COMPLIANCE,
    REGULATORY_NOTICES,
    STATUTORY_DUES,
    TAX_PAYMENT,
)


class ComplianceAssessor(
    BaseAssessor[ComplianceFeatures]
):

    COMPONENT_NAME = "Compliance"
    COMPONENT_WEIGHT = 0.20
    DEFAULT_CONFIDENCE = 100.0

    def assess(
        self,
        features: ComplianceFeatures,
    ) -> AssessmentResult:

        metrics = self._evaluate_metrics(features)

        overall_score = self._calculate_score(metrics)

        return AssessmentResult(
            component=self._build_component_score(overall_score),
            metrics=metrics,
            derived_features=self._build_derived_features(features),
            positive_signals=self._build_positive_signals(features),
            negative_signals=self._build_negative_signals(features),
            warnings=self._build_warnings(features),
        )

    def _evaluate_metrics(
        self,
        features: ComplianceFeatures,
    ):

        return [

            MetricEvaluator.evaluate(
                features.gst_compliance_score,
                GST_RETURN_FILING,
            ),

            MetricEvaluator.evaluate(
                features.epfo_compliance_score,
                EPFO_COMPLIANCE,
            ),

            MetricEvaluator.evaluate(
                features.tax_payment_score,
                TAX_PAYMENT,
            ),

            MetricEvaluator.evaluate(
                features.regulatory_score,
                REGULATORY_NOTICES,
            ),

            MetricEvaluator.evaluate(
                features.statutory_score,
                STATUTORY_DUES,
            ),

            MetricEvaluator.evaluate(
                features.overall_compliance_rate,
                OVERALL_COMPLIANCE,
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
        features: ComplianceFeatures,
    ) -> DerivedFeatures:

        return DerivedFeatures(
            values={
                "gst_compliance_score": features.gst_compliance_score,
                "epfo_compliance_score": features.epfo_compliance_score,
                "tax_payment_score": features.tax_payment_score,
                "regulatory_score": features.regulatory_score,
                "statutory_score": features.statutory_score,
                "overall_compliance_rate": features.overall_compliance_rate,
                "gst_return_filing_rate": features.gst_return_filing_rate,
                "epfo_compliance_rate": features.epfo_compliance_rate,
                "tax_payment_delay_days": features.tax_payment_delay_days,
                "regulatory_notices": features.regulatory_notices,
            }
        )

    def _build_positive_signals(
        self,
        features: ComplianceFeatures,
    ) -> list[str]:

        signals = []

        if features.gst_return_filing_rate >= 0.95:
            signals.append(
                "GST filings are consistently on time."
            )

        if features.epfo_compliance_score >= 95:
            signals.append(
                "EPFO compliance is excellent."
            )

        if not features.statutory_dues_pending:
            signals.append(
                "No pending statutory dues."
            )

        if features.regulatory_notices == 0:
            signals.append(
                "No regulatory notices."
            )

        return signals

    def _build_negative_signals(
        self,
        features: ComplianceFeatures,
    ) -> list[str]:

        signals = []

        if features.gst_return_filing_rate < 0.80:
            signals.append(
                "GST filing compliance is below target."
            )

        if features.tax_payment_delay_days > 0:
            signals.append(
                "Tax payment delays detected."
            )

        if features.statutory_dues_pending:
            signals.append(
                "Pending statutory dues exist."
            )

        if features.regulatory_notices > 1:
            signals.append(
                "Multiple regulatory notices observed."
            )

        return signals

    def _build_warnings(
        self,
        features: ComplianceFeatures,
    ) -> list[str]:

        warnings = []

        if features.overall_compliance_rate < 60:
            warnings.append(
                "Overall compliance is materially below expected levels."
            )

        if features.regulatory_notices > 0:
            warnings.append(
                "Regulatory notices require management attention."
            )

        return warnings
