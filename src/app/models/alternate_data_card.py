from app.models.enums import AlternateDataStatus

from app.models.base import AppBaseModel

class AlternateDataCard(AppBaseModel):
    name: str
    score: float
    status: AlternateDataStatus
    metric: str | None = None
    value: float | None = None