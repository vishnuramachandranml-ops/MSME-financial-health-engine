from __future__ import annotations

from pydantic import Field

from app.models.base import AppBaseModel


class FinancialPosition(AppBaseModel):
    total_assets: float | None = Field(default=None, ge=0)

    total_liabilities: float | None = Field(default=None, ge=0)

    book_value: float | None = None

    working_capital: float | None = None

    current_assets: float | None = Field(default=None, ge=0)

    current_liabilities: float | None = Field(default=None, ge=0)