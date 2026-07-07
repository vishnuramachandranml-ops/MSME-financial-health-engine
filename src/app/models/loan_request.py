from __future__ import annotations

from pydantic import Field

from app.models.base import AppBaseModel
from app.models.enums import CollateralType, LoanType


class Collateral(AppBaseModel):
    available: bool

    collateral_type: CollateralType = CollateralType.NONE

    estimated_value: float | None = Field(
        default=None,
        ge=0,
    )


class LoanRequest(AppBaseModel):
    loan_type: LoanType

    requested_amount: float = Field(
        ...,
        gt=0,
    )

    loan_tenure_months: int = Field(
        ...,
        gt=0,
    )

    loan_purpose: str

    collateral: Collateral | None = None