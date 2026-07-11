from __future__ import annotations

from pydantic import Field

from app.models.base import AppBaseModel
from app.models.business_profile import BusinessProfile
from app.models.cashflow import CashFlow
from app.models.operations import Operations
from app.models.alternate_data import AlternateData
from app.models.compliance import Compliance
from app.models.financial_position import FinancialPosition
from app.models.loan_request import LoanRequest

from pydantic import ConfigDict

from app.examples.swagger_examples import (
    HEALTHY_MANUFACTURING,
    MEDIUM_RISK_MANUFACTURING,
    HIGH_RISK_MANUFACTURING,
    NEW_TO_CREDIT,
)

class AssessmentMetadata(AppBaseModel):
    """
    Request metadata.
    """

    request_id: str | None = Field(
        default=None,
        description="Optional client request identifier."
    )

    source_system: str | None = Field(
        default="API"
    )

    model_version: str | None = Field(
        default="1.0"
    )


class AssessmentRequest(AppBaseModel):

    metadata: AssessmentMetadata = Field(
        default_factory=AssessmentMetadata
    )

    business_profile: BusinessProfile

    cashflow: CashFlow | None = None

    operations: Operations | None = None

    alternate_data: AlternateData | None = None

    compliance: Compliance | None = None

    financial_position: FinancialPosition | None = None

    loan_request: LoanRequest | None = None
