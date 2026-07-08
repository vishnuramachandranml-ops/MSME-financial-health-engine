from __future__ import annotations

from app.engine.assessors.cashflow.assessor import CashFlowAssessor
from app.engine.feature_engineering.cashflow.engineer import CashFlowFeatureEngineer
from app.engine.models.assessment_result import AssessmentResult
from app.models.assessment_request import AssessmentRequest


class AssessmentPipeline:
    """
    Orchestrates the financial assessment workflow.
    """

    def __init__(self) -> None:
        self._cashflow_engineer = CashFlowFeatureEngineer()
        self._cashflow_assessor = CashFlowAssessor()

    def assess(
        self,
        request: AssessmentRequest,
    ) -> AssessmentResult:
        """
        Execute the assessment pipeline.
        """

        cashflow_features = self._cashflow_engineer.transform(
            request.cashflow
        )

        return self._cashflow_assessor.assess(
            cashflow_features
        )