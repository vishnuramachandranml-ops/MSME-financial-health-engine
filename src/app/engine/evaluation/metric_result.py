from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class MetricResult:
    """
    Result of evaluating one business metric.
    """

    metric: str

    value: float

    score: float

    weight: float