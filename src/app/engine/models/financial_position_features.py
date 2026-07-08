from __future__ import annotations

from app.models.base import AppBaseModel


class FinancialPositionFeatures(AppBaseModel):
    """
    Derived financial position features used for assessment.
    """

    current_ratio: float

    debt_to_equity_ratio: float

    working_capital: float

    net_worth: float

    asset_coverage_ratio: float

    fixed_asset_ratio: float

    debt_ratio: float