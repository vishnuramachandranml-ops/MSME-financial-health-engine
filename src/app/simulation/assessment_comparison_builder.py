from __future__ import annotations

from app.models.assessment_response import AssessmentResponse
from app.models.component_breakdown import (
    ComponentBreakdown,
    MetricBreakdown,
)
from app.models.simulation import (
    Impact,
    MetricChange,
    Simulation,
    SimulationInsight,
    TopImpactDriver,
)


class AssessmentComparisonBuilder:
    """
    Builds the Scenario Analysis section by comparing two
    assessment responses.
    """

    def build(
        self,
        before: AssessmentResponse,
        after: AssessmentResponse,
    ) -> Simulation:

        metric_changes = self._build_metric_changes(
            before,
            after,
        )

        top_impact_drivers = self._build_top_impact_drivers(
            metric_changes,
        )

        insight = self._build_simulation_insight(
            before,
            after,
            metric_changes,
            top_impact_drivers,
        )

        return Simulation(
            metric_changes=metric_changes,
            top_impact_drivers=top_impact_drivers,
            insight=insight,
        )

    def _build_metric_changes(
        self,
        before: AssessmentResponse,
        after: AssessmentResponse,
    ) -> list[MetricChange]:

        changes: list[MetricChange] = []

        before_components = {
            component.component: component
            for component in before.component_breakdown
        }

        after_components = {
            component.component: component
            for component in after.component_breakdown
        }

        common_components = (
            before_components.keys()
            & after_components.keys()
        )

        for component_name in sorted(common_components):

            before_component = before_components[component_name]
            after_component = after_components[component_name]

            before_metrics = self._index_metrics(
                before_component,
            )

            after_metrics = self._index_metrics(
                after_component,
            )

            common_metrics = (
                before_metrics.keys()
                & after_metrics.keys()
            )

            for metric_name in sorted(common_metrics):

                before_metric = before_metrics[metric_name]
                after_metric = after_metrics[metric_name]

                value_change = self._difference(
                    before_metric.value,
                    after_metric.value,
                )

                score_change = self._difference(
                    before_metric.score,
                    after_metric.score,
                )

                # Only include metrics that actually changed
                if value_change != 0 or score_change != 0:

                    changes.append(
                        MetricChange(
                            component=component_name,
                            metric=metric_name,
                            before_value=before_metric.value,
                            after_value=after_metric.value,
                            value_change=value_change,
                            before_score=before_metric.score,
                            after_score=after_metric.score,
                            score_change=score_change,
                            impact=self._determine_impact(
                                score_change,
                            ),
                        )
                    )

        return changes

    def _build_top_impact_drivers(
        self,
        metric_changes: list[MetricChange],
    ) -> list[TopImpactDriver]:

        sorted_changes = sorted(
            (
                m
                for m in metric_changes
                if m.score_change != 0
            ),
            key=lambda x: abs(x.score_change),
            reverse=True,
        )

        return [
            TopImpactDriver(
                component=m.component,
                metric=m.metric,
                before_score=m.before_score,
                after_score=m.after_score,
                score_change=m.score_change,
                impact=m.impact,
            )
            for m in sorted_changes[:3]
        ]

    def _build_simulation_insight(
        self,
        before: AssessmentResponse,
        after: AssessmentResponse,
        metric_changes: list[MetricChange],
        top_impact_drivers: list[TopImpactDriver],
    ) -> SimulationInsight:

        before_score = (
            before.summary.financial_health_score or 0
        )

        after_score = (
            after.summary.financial_health_score or 0
        )

        score_change = round(
            after_score - before_score,
            2,
        )

        if score_change > 0:
            headline = "Financial Health Improved"
        elif score_change < 0:
            headline = "Financial Health Declined"
        else:
            headline = "Financial Health Unchanged"

        summary = (
            f"The financial health score changed "
            f"from {before_score:.2f} to "
            f"{after_score:.2f} "
            f"({score_change:+.2f})."
        )

        before_risk = (
            before.summary.risk_level.value
            if before.summary.risk_level
            else "UNKNOWN"
        )

        after_risk = (
            after.summary.risk_level.value
            if after.summary.risk_level
            else "UNKNOWN"
        )

        business_impact = (
            f"Risk level changed from "
            f"{before_risk} to {after_risk}."
        )

        if top_impact_drivers:

            drivers = ", ".join(
                driver.metric
                for driver in top_impact_drivers
            )

            recommendation = (
                "Primary contributors: "
                f"{drivers}. "
            )

            if score_change > 0:
                recommendation += (
                    "The simulated scenario indicates "
                    "improved creditworthiness."
                )
            elif score_change < 0:
                recommendation += (
                    "Review the modified parameters "
                    "before proceeding."
                )
            else:
                recommendation += (
                    "The simulated scenario does not "
                    "materially change the assessment."
                )

        else:

            recommendation = (
                "No significant assessment changes "
                "were observed."
            )

        return SimulationInsight(
            headline=headline,
            summary=summary,
            business_impact=business_impact,
            recommendation=recommendation,
        )

    @staticmethod
    def _index_metrics(
        component: ComponentBreakdown,
    ) -> dict[str, MetricBreakdown]:

        return {
            metric.metric: metric
            for metric in component.metrics
        }

    @staticmethod
    def _difference(
        before: float,
        after: float,
    ) -> float:

        return round(after - before, 2)

    @staticmethod
    def _determine_impact(
        score_change: float,
    ) -> Impact:

        if score_change > 0:
            return "positive"

        if score_change < 0:
            return "negative"

        return "neutral"