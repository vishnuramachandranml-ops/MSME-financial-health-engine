from app.engine.feature_engineering.compliance.calculator import (
    ComplianceCalculator,
)
from app.engine.feature_engineering.compliance.constants import (
    DEFAULT_COMPLIANCE_RATE,
    DEFAULT_DELAY_DAYS,
    DEFAULT_REGULATORY_NOTICES,
)
from app.engine.interfaces.base_feature_engineer import BaseFeatureEngineer
from app.engine.models.compliance_features import ComplianceFeatures
from app.models.compliance import Compliance


class ComplianceFeatureEngineer(
    BaseFeatureEngineer[Compliance, ComplianceFeatures]
):
    """
    Converts Compliance input into engine-ready features.
    """

    def transform(
        self,
        data: Compliance,
    ) -> ComplianceFeatures:

        gst_return_filing_rate = self._rate(
            data.gst_return_filing_rate
        )
        epfo_compliance_rate = self._rate(
            data.epfo_compliance_rate
        )
        tax_payment_delay_days = self._days(
            data.tax_payment_delay_days
        )
        regulatory_notices = self._notices(
            data.regulatory_notices
        )

        gst_compliance_score = ComplianceCalculator.calculate_gst_score(
            data.gst_registered,
            gst_return_filing_rate,
        )
        epfo_compliance_score = ComplianceCalculator.calculate_epfo_score(
            data.epfo_registered,
            epfo_compliance_rate,
        )
        tax_payment_score = ComplianceCalculator.calculate_tax_delay_score(
            tax_payment_delay_days,
        )
        regulatory_score = ComplianceCalculator.calculate_regulatory_score(
            regulatory_notices,
        )
        statutory_score = ComplianceCalculator.calculate_statutory_score(
            data.statutory_dues_pending,
        )

        return ComplianceFeatures(
            gst_compliance_score=gst_compliance_score,
            epfo_compliance_score=epfo_compliance_score,
            tax_payment_score=tax_payment_score,
            regulatory_score=regulatory_score,
            statutory_score=statutory_score,
            overall_compliance_rate=ComplianceCalculator.calculate_overall_compliance(
                [
                    gst_compliance_score,
                    epfo_compliance_score,
                    tax_payment_score,
                    regulatory_score,
                    statutory_score,
                ]
            ),
            gst_return_filing_rate=gst_return_filing_rate,
            epfo_compliance_rate=epfo_compliance_rate,
            tax_payment_delay_days=tax_payment_delay_days,
            regulatory_notices=regulatory_notices,
            statutory_dues_pending=data.statutory_dues_pending,
        )

    def _rate(
        self,
        value: float | None,
    ) -> float:

        return value if value is not None else DEFAULT_COMPLIANCE_RATE

    def _days(
        self,
        value: int | None,
    ) -> int:

        return value if value is not None else DEFAULT_DELAY_DAYS

    def _notices(
        self,
        value: int | None,
    ) -> int:

        return value if value is not None else DEFAULT_REGULATORY_NOTICES
