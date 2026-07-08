from __future__ import annotations

from app.engine.assessors.compliance.assessor import ComplianceAssessor
from app.engine.models.compliance_features import ComplianceFeatures


def test_compliance_assessor_returns_assessment_result():
    result = ComplianceAssessor().assess(
        ComplianceFeatures(
            gst_compliance_score=100,
            epfo_compliance_score=100,
            tax_payment_score=100,
            regulatory_score=100,
            statutory_score=100,
            overall_compliance_rate=100,
            gst_return_filing_rate=1.0,
            epfo_compliance_rate=1.0,
            tax_payment_delay_days=0,
            regulatory_notices=0,
            statutory_dues_pending=False,
        )
    )

    assert result.component.name == "Compliance"
    assert result.component.score == 100
    assert len(result.metrics) == 6
    assert result.derived_features.values["overall_compliance_rate"] == 100
    assert result.positive_signals
    assert not result.negative_signals
    assert not result.warnings
