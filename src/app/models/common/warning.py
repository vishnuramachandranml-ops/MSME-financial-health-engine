from pydantic import Field

from app.models.base import AppBaseModel


class WarningMessage(AppBaseModel):
    code: str = Field(...)
    message: str = Field(...)