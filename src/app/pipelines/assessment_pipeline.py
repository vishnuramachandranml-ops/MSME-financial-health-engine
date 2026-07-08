from __future__ import annotations

from app.engine.assessors.cashflow.assessor import CashFlowAssessor
from app.engine.assessors.financial_position.assessor import (
    FinancialPositionAssessor,
)
from app.engine.feature_engineering.cashflow.engineer import CashFlowFeatureEngineer
from app.engine.feature_engineering.financial_position.engineer import (
    FinancialPositionFeatureEngineer,
)
from app.engine.models.assessment_result import AssessmentResult
from app.models.assessment_request import AssessmentRequest


class AssessmentPipeline:
    """
    Orchestrates the financial assessment workflow.
    """

    def __init__(self) -> None:
        self._cashflow_engineer = CashFlowFeatureEngineer()
        self._cashflow_assessor = CashFlowAssessor()
        self._financial_position_engineer = FinancialPositionFeatureEngineer()
        self._financial_position_assessor = FinancialPositionAssessor()

    def assess(
        self,
        request: AssessmentRequest,
    ) -> AssessmentResult:
        """
        Execute the assessment pipeline.
        """

        if request.financial_position is not None:
            financial_position_features = self._financial_position_engineer.transform(
                request.financial_position
            )

            return self._financial_position_assessor.assess(
                financial_position_features
            )

        cashflow_features = self._cashflow_engineer.transform(
            request.cashflow
        )

        return self._cashflow_assessor.assess(
            cashflow_features
        )
