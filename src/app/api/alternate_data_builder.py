from __future__ import annotations

from app.models.alternate_data_card import AlternateDataCard
from app.models.component_breakdown import ComponentBreakdown
from app.models.enums import AlternateDataStatus


CARD_METRICS = {
    "GST": "GST Filing Rate",
    "EPFO": "EPFO Compliance",
    "UPI": "Digital Payment Ratio",
    "Electricity": "Electricity Stability",
    "Fuel": "Fuel Stability",
    "Sales": "Sales Growth",
    "Purchase": "Purchase Growth",
    "Bank": "Average Bank Balance",
}


class AlternateDataBuilder:
    """
    Builds the Alternate Data cards displayed on the dashboard.
    """

    def build(
        self,
        component_breakdown: list[ComponentBreakdown],
    ) -> list[AlternateDataCard]:

        metric_lookup = {}

        for component in component_breakdown:

            for metric in component.metrics:

                metric_lookup[metric.metric] = metric

        cards: list[AlternateDataCard] = []

        for card_name, metric_name in CARD_METRICS.items():

            metric = metric_lookup.get(metric_name)

            if metric is None:
                continue

            cards.append(

                AlternateDataCard(
                    name=card_name,
                    score=round(metric.score, 2),
                    status=self._get_status(metric.score),
                    metric=metric.metric,
                    value=metric.value,
                )

            )

        return cards

    def _get_status(
        self,
        score: float,
    ) -> AlternateDataStatus:

        if score >= 95:
            return AlternateDataStatus.EXCELLENT

        if score >= 80:
            return AlternateDataStatus.GOOD

        if score >= 60:
            return AlternateDataStatus.AVERAGE

        return AlternateDataStatus.NEEDS_IMPROVEMENT