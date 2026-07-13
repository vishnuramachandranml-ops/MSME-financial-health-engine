from __future__ import annotations

from app.engine.recommendations.recommendation_engine import (
    RecommendationEngine,
)
from app.engine.risk.risk_classifier import RiskClassifier

from app.llm.summary_service import SummaryService

from app.models.assessment_request import AssessmentRequest
from app.models.assessment_response import (
    AssessmentResponse,
    AssessmentSummary,
)

from app.models.component_breakdown import (
    ComponentBreakdown,
    MetricBreakdown,
)

from app.engine.models.component_score import ComponentScore

from app.models.enums import AssessmentStatus

from app.models.simulation_inputs import (
    AlternateDataSimulation,
    CashFlowSimulation,
    ComplianceSimulation,
    FinancialPositionSimulation,
    OperationsSimulation,
    SimulationInputs,
)

from app.engine.decision.decision_engine import DecisionEngine


def build_assessment_response(
    request: AssessmentRequest,
    result,
) -> AssessmentResponse:

    risk_level = RiskClassifier.classify(
        result.component.score
    )

    recommendations = RecommendationEngine.generate(
        result
    )

    llm_analysis = SummaryService().summarize(
        result=result,
        risk_level=risk_level.value,
        recommendations=recommendations,
    )

    score = result.component.score

    requested_amount = (
        request.loan_request.requested_amount
        if request.loan_request
        else 0
    )

    credit_decision = DecisionEngine.credit_decision(
        score
    )

    suggested_amount = DecisionEngine.suggested_loan_amount(
        score,
        requested_amount,
    )

    loan_min, loan_max = DecisionEngine.loan_limit_range(
        suggested_amount
    )

    summary = AssessmentSummary(

        financial_health_score=score,

        risk_level=risk_level,

        confidence_score=result.component.confidence,

        credit_decision=credit_decision,

        suggested_loan_amount=suggested_amount,

        loan_limit_min=loan_min,

        loan_limit_max=loan_max,

        monitoring_frequency=DecisionEngine.monitoring_frequency(
            score
        ),

        risk_grade=DecisionEngine.risk_grade(
            score
        ),
    )

    component_breakdown = []

    for assessment in result.component_assessments:

        component_breakdown.append(

            ComponentBreakdown(

                component=assessment.component.name,

                score=assessment.component.score,

                confidence=assessment.component.confidence,

                metrics=[

                    MetricBreakdown(

                        metric=metric.metric,

                        value=metric.value,

                        score=metric.score,

                        weight=metric.weight,

                    )

                    for metric in assessment.metrics

                ],

                positive_signals=assessment.positive_signals,

                negative_signals=assessment.negative_signals,

            )

        )

    derived = result.derived_features.values

    simulation_inputs = SimulationInputs(

        cashflow=CashFlowSimulation(

            revenue_growth=derived.get("revenue_growth"),

            operating_margin=(
                derived.get("operating_margin") * 100
                if derived.get("operating_margin") is not None
                else None
            ),

            expense_ratio=(
                derived.get("expense_ratio") * 100
                if derived.get("expense_ratio") is not None
                else None
            ),

            collection_days=derived.get(
                "collection_days"
            ),
        ),

        financial_position=FinancialPositionSimulation(

            current_ratio=derived.get(
                "current_ratio"
            ),

            debt_asset_ratio=(
                derived.get("debt_ratio") * 100
                if derived.get("debt_ratio") is not None
                else None
            ),

            working_capital=derived.get(
                "working_capital"
            ),
        ),

        operations=OperationsSimulation(
            sales_growth=derived.get("sales_growth"),
            capacity_utilization=(
                derived.get("capacity_utilization") * 100
                if derived.get("capacity_utilization") is not None
                else None
            ),
        ),

        compliance=ComplianceSimulation(

            gst_filing_rate=(
                derived.get("gst_filing_rate")
                * 100
                if derived.get(
                    "gst_filing_rate"
                )
                is not None
                else None
            ),

            epfo_compliance_rate=(
                derived.get(
                    "epfo_compliance_rate"
                )
                * 100
                if derived.get(
                    "epfo_compliance_rate"
                )
                is not None
                else None
            ),

            tax_delay_days=derived.get(
                "tax_payment_delay_days"
            ),
        ),

        alternate_data=AlternateDataSimulation(

            digital_payment_ratio=(
                derived.get(
                    "digital_payment_ratio"
                )
                * 100
                if derived.get(
                    "digital_payment_ratio"
                )
                is not None
                else None
            ),

            average_bank_balance=derived.get(
                "average_bank_balance"
            ),
        ),
    )

    return AssessmentResponse(

        request_id=request.metadata.request_id,

        status=AssessmentStatus.SUCCESS,

        summary=summary,

        component_scores=result.component_scores,

        component_breakdown=component_breakdown,

        positive_signals=result.positive_signals,

        negative_signals=result.negative_signals,

        recommendations=recommendations,

        warnings=result.warnings,

        simulation_inputs=simulation_inputs,

        llm_analysis=llm_analysis,
    )