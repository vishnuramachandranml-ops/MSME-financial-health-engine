from __future__ import annotations

from app.engine.feature_engineering.compliance.calculator import (
    ComplianceCalculator,
)


def test_compliance_calculator_derives_scores():
    assert ComplianceCalculator.calculate_gst_score(True, 0.95) == 95
    assert ComplianceCalculator.calculate_gst_score(False, 0.95) == 0
    assert ComplianceCalculator.calculate_epfo_score(True, 0.90) == 90
    assert ComplianceCalculator.calculate_epfo_score(False, 0.90) == 100
    assert ComplianceCalculator.calculate_tax_delay_score(10) == 80
    assert ComplianceCalculator.calculate_regulatory_score(2) == 50
    assert ComplianceCalculator.calculate_statutory_score(False) == 100
    assert ComplianceCalculator.calculate_statutory_score(True) == 40
    assert ComplianceCalculator.calculate_overall_compliance(
        [
            100,
            90,
            80,
        ]
    ) == 90
