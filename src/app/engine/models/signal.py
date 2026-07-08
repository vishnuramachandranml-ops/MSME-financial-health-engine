from pydantic import Field

from app.models.base import AppBaseModel


class Signal(AppBaseModel):
    feature: str
    message: str
    impact: float