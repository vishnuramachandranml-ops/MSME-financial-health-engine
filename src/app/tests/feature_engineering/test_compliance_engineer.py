from __future__ import annotations

from app.engine.feature_engineering.compliance.engineer import (
    ComplianceFeatureEngineer,
)
from app.models.compliance import Compliance


def test_compliance_engineer_derives_features():
    features = ComplianceFeatureEngineer().transform(
        Compliance(
            gst_registered=True,
            gst_return_filing_rate=0.90,
            epfo_registered=True,
            epfo_compliance_rate=0.95,
            tax_payment_delay_days=10,
            statutory_dues_pending=True,
            regulatory_notices=2,
        )
    )

    assert features.gst_compliance_score == 90
    assert features.epfo_compliance_score == 95
    assert features.tax_payment_score == 80
    assert features.regulatory_score == 50
    assert features.statutory_score == 40
    assert features.overall_compliance_rate == 71
    assert features.tax_payment_delay_days == 10
    assert features.regulatory_notices == 2
    assert features.statutory_dues_pending is True


def test_compliance_engineer_uses_default_values():
    features = ComplianceFeatureEngineer().transform(
        Compliance()
    )

    assert features.gst_compliance_score == 100
    assert features.epfo_compliance_score == 100
    assert features.tax_payment_score == 100
    assert features.regulatory_score == 100
    assert features.statutory_score == 100
    assert features.overall_compliance_rate == 100
