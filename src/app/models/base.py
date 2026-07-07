from __future__ import annotations

from pydantic import BaseModel, ConfigDict


class AppBaseModel(BaseModel):
    """
    Base model for all application models.
    """

    model_config = ConfigDict(
        extra="forbid",
        validate_assignment=True,
        populate_by_name=True,
        str_strip_whitespace=True,
        use_enum_values=False,
        frozen=False,
    )