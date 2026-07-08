from __future__ import annotations

from pydantic import Field

from app.models.base import AppBaseModel
from app.models.enums import IndustryType


class BusinessProfile(AppBaseModel):
    """
    Basic MSME information.
    """

    business_id: str = Field(
        ...,
        description="Unique business identifier",
        examples=["MSME001"],
    )

    business_name: str = Field(
        ...,
        description="Registered business name",
        examples=["ABC Engineering Works"],
    )

    industry: IndustryType = Field(
        default=IndustryType.MANUFACTURING,
        description="Industry sector",
    )

    business_type: str = Field(
        ...,
        description="Ownership type",
        examples=["Private Limited"],
    )

    msme_registered: bool = Field(
        default=True,
        description="Whether the business is registered as an MSME.",
    )

    udyam_registration_number: str | None = Field(
        default=None,
        description="Official Udyam registration number.",
    )

    business_age_years: int = Field(
        ...,
        ge=0,
        le=100,
    )

    employee_count: int = Field(
        ...,
        ge=0,
    )

    annual_turnover: float = Field(
        ...,
        ge=0,
    )

    location: str