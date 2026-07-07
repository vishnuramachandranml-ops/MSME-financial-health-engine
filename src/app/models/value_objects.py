from __future__ import annotations

from statistics import mean

from pydantic import Field, field_validator

from app.models.base import AppBaseModel


class MonthlyTimeSeries(AppBaseModel):
    """
    Represents six months of chronological business data.
    """

    values: list[float] = Field(
        ...,
        min_length=6,
        max_length=6,
        description="Exactly six monthly values ordered oldest to newest.",
        examples=[[100000, 105000, 110000, 120000, 125000, 130000]],
    )

    @field_validator("values")
    @classmethod
    def validate_values(cls, values: list[float]) -> list[float]:
        if any(value < 0 for value in values):
            raise ValueError("Monthly values cannot be negative.")
        return values

    @property
    def latest(self) -> float:
        return self.values[-1]

    @property
    def oldest(self) -> float:
        return self.values[0]

    @property
    def average(self) -> float:
        return mean(self.values)

    @property
    def minimum(self) -> float:
        return min(self.values)

    @property
    def maximum(self) -> float:
        return max(self.values)