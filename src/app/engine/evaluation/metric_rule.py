from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class MetricRule:
    """
    Configuration describing how a business metric should be scored.
    """

    metric: str

    description: str

    weight: float

    thresholds: tuple[tuple[float, float], ...]

    inverse: bool = False