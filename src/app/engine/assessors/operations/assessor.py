from __future__ import annotations

from app.engine.evaluation.metric_evaluator import MetricEvaluator
from app.engine.models.assessment_result import AssessmentResult
from app.engine.models.component_score import ComponentScore
from app.engine.models.derived_features import DerivedFeatures
from app.engine.models.operations_features import OperationsFeatures
from app.engine.scoring.weighted_scorer import WeightedScorer
from app.engine.scorecards.operations_scorecard import (
    SALES_GROWTH,
    PURCHASE_GROWTH,
    REPEAT_CUSTOMERS,
    VENDOR_DIVERSIFICATION,
    CUSTOMER_DIVERSIFICATION,
    CAPACITY_UTILIZATION,
    ORDER_FULFILLMENT,
    OPERATIONAL_EFFICIENCY,
)


class OperationsAssessor:

    COMPONENT_NAME = "Operations"
    COMPONENT_WEIGHT = 0.15
    DEFAULT_CONFIDENCE = 100.0

    def assess(
        self,
        features: OperationsFeatures,
    ) -> AssessmentResult:

        metrics = self._evaluate_metrics(features)

        overall_score = self._calculate_score(metrics)

        return AssessmentResult(
            component=self._build_component_score(
                overall_score
            ),
            metrics=metrics,
            derived_features=self._build_derived_features(
                features
            ),
            positive_signals=self._build_positive_signals(
                features
            ),
            negative_signals=self._build_negative_signals(
                features
            ),
            warnings=[],
        )

    def _evaluate_metrics(
        self,
        features: OperationsFeatures,
    ):

        return [

            MetricEvaluator.evaluate(
                features.sales_growth,
                SALES_GROWTH,
            ),

            MetricEvaluator.evaluate(
                features.purchase_growth,
                PURCHASE_GROWTH,
            ),

            MetricEvaluator.evaluate(
                features.repeat_customer_ratio,
                REPEAT_CUSTOMERS,
            ),

            MetricEvaluator.evaluate(
                features.vendor_diversification_score,
                VENDOR_DIVERSIFICATION,
            ),

            MetricEvaluator.evaluate(
                features.customer_diversification_score,
                CUSTOMER_DIVERSIFICATION,
            ),

            MetricEvaluator.evaluate(
                features.capacity_utilization,
                CAPACITY_UTILIZATION,
            ),

            MetricEvaluator.evaluate(
                features.order_fulfillment_rate,
                ORDER_FULFILLMENT,
            ),

            MetricEvaluator.evaluate(
                features.operational_efficiency_score,
                OPERATIONAL_EFFICIENCY,
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
        features: OperationsFeatures,
    ) -> DerivedFeatures:

        return DerivedFeatures(
            values={
                "sales_growth": features.sales_growth,
                "purchase_growth": features.purchase_growth,
                "monthly_sales_average": features.monthly_sales_average,
                "monthly_purchase_average": features.monthly_purchase_average,
                "vendor_diversification_score": features.vendor_diversification_score,
                "customer_diversification_score": features.customer_diversification_score,
                "capacity_utilization": features.capacity_utilization,
                "inventory_turnover": features.inventory_turnover,
                "order_fulfillment_rate": features.order_fulfillment_rate,
                "employee_productivity": features.employee_productivity,
                "operational_efficiency_score": features.operational_efficiency_score,
            }
        )

    def _build_positive_signals(
        self,
        features: OperationsFeatures,
    ) -> list[str]:

        signals = []

        if features.sales_growth >= 10:
            signals.append(
                "Operational sales activity is increasing steadily."
            )

        if features.repeat_customer_ratio >= 0.70:
            signals.append(
                "Business has a strong repeat customer base."
            )

        if features.capacity_utilization >= 0.80:
            signals.append(
                "Operational capacity is well utilized."
            )

        if features.order_fulfillment_rate >= 0.95:
            signals.append(
                "Customer orders are fulfilled consistently."
            )

        return signals

    def _build_negative_signals(
        self,
        features: OperationsFeatures,
    ) -> list[str]:

        signals = []

        if features.sales_growth < 0:
            signals.append(
                "Sales are declining."
            )

        if features.capacity_utilization < 0.50:
            signals.append(
                "Operational capacity utilization is low."
            )

        if features.order_fulfillment_rate < 0.85:
            signals.append(
                "Order fulfillment performance needs improvement."
            )

        if features.repeat_customer_ratio < 0.40:
            signals.append(
                "Repeat customer ratio is below the expected level."
            )

        return signals