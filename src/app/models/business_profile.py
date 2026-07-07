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

    business_age_years: int = Field(
        ...,
        ge=0,
        le=100,
        description="Age of business in years",
        examples=[8],
    )

    employee_count: int = Field(
        ...,
        ge=0,
        description="Total employees",
        examples=[42],
    )

    annual_turnover: float = Field(
        ...,
        ge=0,
        description="Annual turnover (INR)",
        examples=[25000000],
    )

    location: str = Field(
        ...,
        examples=["Hosur, Tamil Nadu"],
    )