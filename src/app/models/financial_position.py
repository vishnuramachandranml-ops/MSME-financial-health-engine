from __future__ import annotations

from pydantic import Field

from app.models.base import AppBaseModel


class FinancialPosition(AppBaseModel):
    """
    Business balance sheet snapshot.
    """

    total_assets: float | None = Field(default=None, ge=0)

    current_assets: float | None = Field(default=None, ge=0)

    fixed_assets: float | None = Field(default=None, ge=0)

    cash_and_bank: float | None = Field(default=None, ge=0)

    inventory: float | None = Field(default=None, ge=0)

    accounts_receivable: float | None = Field(default=None, ge=0)

    total_liabilities: float | None = Field(default=None, ge=0)

    current_liabilities: float | None = Field(default=None, ge=0)

    long_term_debt: float | None = Field(default=None, ge=0)

    net_worth: float | None = None

    book_value: float | None = None

    working_capital: float | None = None