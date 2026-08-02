from __future__ import annotations

from dataclasses import dataclass

from app.models.assessment_response import AssessmentResponse
from app.models.component_breakdown import MetricBreakdown


@dataclass(frozen=True)
class MetricKey:
    """
    Unique identifier for a metric within an assessment.
    """

    component: str
    metric: str


def extract_metrics(
    assessment: AssessmentResponse,
) -> dict[MetricKey, MetricBreakdown]:
    """
    Flattens the component breakdown into a dictionary for
    O(1) metric lookup.

    Example
    -------
    {
        MetricKey("Cash Flow", "Revenue Growth"):
            MetricBreakdown(...),

        MetricKey("Cash Flow", "Operating Margin"):
            MetricBreakdown(...),
    }
    """

    metrics: dict[MetricKey, MetricBreakdown] = {}

    for component in assessment.component_breakdown:
        for metric in component.metrics:
            metrics[
                MetricKey(
                    component=component.component,
                    metric=metric.metric,
                )
            ] = metric

    return metrics