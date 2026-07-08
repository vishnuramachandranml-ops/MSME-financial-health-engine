from pydantic import Field

from app.models.base import AppBaseModel


class ScoreBreakdown(AppBaseModel):
    metric: str
    value: float
    score: float
    weight: float