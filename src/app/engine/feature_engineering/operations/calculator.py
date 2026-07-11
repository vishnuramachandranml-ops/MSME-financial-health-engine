from __future__ import annotations

from statistics import mean

from app.models.operations import Operations
from app.models.value_objects import MonthlyTimeSeries
from app.engine.models.operations_features import OperationsFeatures

class OperationsCalculator:
    """
    Utility class for computing derived operational metrics.
    """

    @staticmethod
    def average(series: MonthlyTimeSeries) -> float:
        values = [value for value in series.values if value is not None]

        if not values:
            return 0.0

        return mean(values)

    @staticmethod
    def growth_rate(series: MonthlyTimeSeries) -> float:
        values = [value for value in series.values if value is not None]

        if len(values) < 2:
            return 0.0

        first = values[0]
        last = values[-1]

        if first <= 0:
            return 0.0

        return ((last - first) / first) * 100

    @staticmethod
    def vendor_diversification_score(vendor_count: int) -> float:
        """
        More vendors generally imply lower supplier concentration risk.
        """

        if vendor_count >= 20:
            return 100

        if vendor_count >= 15:
            return 85

        if vendor_count >= 10:
            return 70

        if vendor_count >= 5:
            return 50

        return 25

    @staticmethod
    def customer_diversification_score(customer_count: int) -> float:
        """
        More customers reduce concentration risk.
        """

        if customer_count >= 100:
            return 100

        if customer_count >= 50:
            return 85

        if customer_count >= 20:
            return 70

        if customer_count >= 10:
            return 50

        return 25

    @staticmethod
    def operational_efficiency_score(
        repeat_customer_ratio: float,
        capacity_utilization: float,
        order_fulfillment_rate: float,
    ) -> float:
        """
        Aggregate operational efficiency score.
        """

        return (
            (
                repeat_customer_ratio
                + capacity_utilization
                + order_fulfillment_rate
            )
            / 3
        ) * 100

    @classmethod
    def calculate(
        cls,
        operations: Operations,
    ) -> dict:
        sales_growth = cls.growth_rate(
            operations.monthly_sales_orders
        )

        purchase_growth = cls.growth_rate(
            operations.monthly_purchase_orders
        )

        monthly_sales_average = cls.average(
            operations.monthly_sales_orders
        )

        monthly_purchase_average = cls.average(
            operations.monthly_purchase_orders
        )

        vendor_score = cls.vendor_diversification_score(
            operations.vendor_count
        )

        customer_score = cls.customer_diversification_score(
            operations.customer_count
        )

        efficiency_score = cls.operational_efficiency_score(
            operations.repeat_customer_ratio or 0,
            operations.capacity_utilization or 0,
            operations.order_fulfillment_rate or 0,
        )


        return OperationsFeatures(
            sales_growth=sales_growth,
            purchase_growth=purchase_growth,
            repeat_customer_ratio=operations.repeat_customer_ratio or 0.0,
            vendor_diversification_score=vendor_score,
            customer_diversification_score=customer_score,
            capacity_utilization=operations.capacity_utilization or 0.0,
            inventory_turnover=operations.inventory_turnover or 0.0,
            order_fulfillment_rate=operations.order_fulfillment_rate or 0.0,
            employee_productivity=operations.employee_productivity or 0.0,
            operational_efficiency_score=efficiency_score,
            monthly_sales_average=monthly_sales_average,
            monthly_purchase_average=monthly_purchase_average,
        )