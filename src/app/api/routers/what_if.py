from __future__ import annotations

from fastapi import APIRouter,Body

from app.api.response_builder import build_assessment_response

from app.models.what_if_request import WhatIfRequest
from app.models.what_if_response import (
    AssessmentDelta,
    ChangedParameter,
    ComponentDelta,
    WhatIfResponse,
)

from app.pipelines.assessment_pipeline import AssessmentPipeline
from app.services.what_if_service import WhatIfService

from app.models.assessment_request import AssessmentRequest
from app.models.simulation_inputs import SimulationInputs


from app.examples.swagger_examples import (
    WHAT_IF_CASHFLOW,
    WHAT_IF_FINANCIAL_POSITION,
    WHAT_IF_COMPLIANCE,
    WHAT_IF_ALL,
)

router = APIRouter(
    prefix="/assessment",
    tags=["FinancialAssessment"],
)

pipeline = AssessmentPipeline()
service = WhatIfService()


@router.post(
    "/what-if",
    response_model=WhatIfResponse,
    summary="Run What-If Simulation",
)
async def what_if(
    request: WhatIfRequest = Body(
        ...,
        openapi_examples={
            "cashflow": {
                "summary": "Improve Cash Flow",
                "description": (
                    "Reduce collection days and improve revenue growth "
                    "to simulate better cash flow."
                ),
                "value": WHAT_IF_CASHFLOW,
            },
            "financial_position": {
                "summary": "Improve Financial Position",
                "description": (
                    "Increase working capital and improve current ratio."
                ),
                "value": WHAT_IF_FINANCIAL_POSITION,
            },
            "compliance": {
                "summary": "Improve Compliance",
                "description": (
                    "Improve GST and EPFO compliance."
                ),
                "value": WHAT_IF_COMPLIANCE,
            },
            "all": {
                "summary": "Overall Business Improvement",
                "description": (
                    "Improve multiple business parameters together."
                ),
                "value": WHAT_IF_ALL,
            },
        },
    ),
):
    # ----------------------------
    # Before Assessment
    # ----------------------------

    before_result = pipeline.assess(
        request.original_request
    )

    before = build_assessment_response(
        request.original_request,
        before_result,
    )

    # ----------------------------
    # Apply Scenario
    # ----------------------------

    modified_request = service.apply(
        request.original_request,
        request.scenario,
    )

    # ----------------------------
    # After Assessment
    # ----------------------------

    after_result = pipeline.assess(
        modified_request,
    )

    after = build_assessment_response(
        modified_request,
        after_result,
    )

    # ----------------------------
    # Component Delta
    # ----------------------------

    before_scores = {
        component.name: component.score
        for component in before_result.component_scores
    }

    component_changes = []

    for component in after_result.component_scores:

        before_score = before_scores.get(
            component.name,
            0,
        )

        component_changes.append(

            ComponentDelta(

                component=component.name,

                before_score=before_score,

                after_score=component.score,

                score_change=round(
                    component.score - before_score,
                    2,
                ),
            )

        )

    # ----------------------------
    # Overall Delta
    # ----------------------------

    delta = AssessmentDelta(

        score_change=round(

            after.summary.financial_health_score
            - before.summary.financial_health_score,

            2,

        ),

        previous_risk=before.summary.risk_level.value,

        new_risk=after.summary.risk_level.value,

        component_changes=component_changes,
    )

    # ----------------------------
    # Changed Parameters
    # ----------------------------

    changed_parameters = [] 

    _collect_changed_parameters(
        request.original_request,
        request.scenario,
        changed_parameters,
    )

    return WhatIfResponse(

        before=before,

        after=after,

        delta=delta,

        changed_parameters=changed_parameters,
    )


def _collect_changed_parameters(
    original: AssessmentRequest,
    scenario: SimulationInputs,
    changes: list[ChangedParameter],
) -> None:

    if scenario.cashflow:
        revenue = sum(original.cashflow.monthly_revenue.values)
        expense = sum(original.cashflow.monthly_expenses.values)
        if scenario.cashflow.revenue_growth is not None:
            first = original.cashflow.monthly_revenue.values[0]
            last = original.cashflow.monthly_revenue.values[-1]

            before_growth = (
                round(((last - first) / first) * 100, 2)
                if first
                else None
            )
            changes.append(
                ChangedParameter(
                    parameter="Revenue Growth (%)",
                    before=before_growth,
                    after=scenario.cashflow.revenue_growth,
                )
            )

        if scenario.cashflow.operating_margin is not None:
            margin = (
                round(((revenue - expense) / revenue) * 100, 2)
                if revenue
                else None
            )
            changes.append(
                ChangedParameter(
                    parameter="Operating Margin (%)",
                    before=margin,
                    after=scenario.cashflow.operating_margin,
                )
            )

        if scenario.cashflow.expense_ratio is not None:
            
            ratio = (
                round((expense / revenue) * 100, 2)
                if revenue
                else None
            )
            changes.append(
                ChangedParameter(
                    parameter="Expense Ratio (%)",
                    before=ratio,
                    after=scenario.cashflow.expense_ratio,
                )
            )

        if scenario.cashflow.collection_days is not None:

            changes.append(
                ChangedParameter(
                    parameter="Collection Days",
                    before=original.cashflow.average_collection_days,
                    after=scenario.cashflow.collection_days,
                )
            )

    if scenario.financial_position:

        if scenario.financial_position.current_ratio is not None:

            changes.append(
                ChangedParameter(
                    parameter="Current Ratio",
                    before=(
                        original.financial_position.current_assets
                        / original.financial_position.current_liabilities
                        if original.financial_position.current_liabilities
                        else None
                    ),
                    after=scenario.financial_position.current_ratio,
                )
            )

        if scenario.financial_position.working_capital is not None:

            changes.append(
                ChangedParameter(
                    parameter="Working Capital",
                    before=original.financial_position.working_capital,
                    after=scenario.financial_position.working_capital,
                )
            )

        if scenario.financial_position.debt_asset_ratio is not None:

            changes.append(
                ChangedParameter(
                    parameter="Debt Ratio (%)",
                    before=(
                        (
                            original.financial_position.total_liabilities
                            / original.financial_position.total_assets
                        ) * 100
                        if original.financial_position.total_assets
                        else None
                    ),
                    after=scenario.financial_position.debt_asset_ratio,
                )
            )

    if scenario.operations:

        if scenario.operations.sales_growth is not None:
            first = original.operations.monthly_sales_orders.values[0]
            last = original.operations.monthly_sales_orders.values[-1]

            before_growth = (
                round(((last - first) / first) * 100, 2)
                if first
                else None
            )
            changes.append(
                ChangedParameter(
                    parameter="Sales Growth (%)",
                    before=before_growth,
                    after=scenario.operations.sales_growth,
                )
            )

        if scenario.operations.capacity_utilization is not None:

            changes.append(
                ChangedParameter(
                    parameter="Capacity Utilization (%)",
                    before=original.operations.capacity_utilization * 100,
                    after=scenario.operations.capacity_utilization,
                )
            )

    if scenario.compliance:

        if scenario.compliance.gst_filing_rate is not None:

            changes.append(
                ChangedParameter(
                    parameter="GST Filing Rate (%)",
                    before=original.compliance.gst_return_filing_rate * 100,
                    after=scenario.compliance.gst_filing_rate,
                )
            )

        if scenario.compliance.epfo_compliance_rate is not None:

            changes.append(
                ChangedParameter(
                    parameter="EPFO Compliance (%)",
                    before=original.compliance.epfo_compliance_rate * 100,
                    after=scenario.compliance.epfo_compliance_rate,
                )
            )

        if scenario.compliance.tax_delay_days is not None:

            changes.append(
                ChangedParameter(
                    parameter="Tax Delay Days",
                    before=original.compliance.tax_payment_delay_days,
                    after=scenario.compliance.tax_delay_days,
                )
            )

    if scenario.alternate_data:

        if scenario.alternate_data.digital_payment_ratio is not None:

            changes.append(
                ChangedParameter(
                    parameter="Digital Payment Ratio (%)",
                    before=original.alternate_data.digital_payment_ratio * 100,
                    after=scenario.alternate_data.digital_payment_ratio,
                )
            )

        if scenario.alternate_data.average_bank_balance is not None:

            changes.append(
                ChangedParameter(
                    parameter="Average Bank Balance",
                    before=original.alternate_data.average_bank_balance,
                    after=scenario.alternate_data.average_bank_balance,
                )
            )