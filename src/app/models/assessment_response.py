from __future__ import annotations

from pydantic import Field

from app.models.base import AppBaseModel
from app.engine.models.component_score import ComponentScore
from app.llm.models import LLMAnalysis
from app.models.component_breakdown import ComponentBreakdown
from app.models.simulation_inputs import SimulationInputs
from app.models.enums import (
    AssessmentStatus,
    RiskLevel)
from app.models.credit_decision import CreditDecision
from app.models.monitoring_frequency import MonitoringFrequency

class AssessmentSummary(AppBaseModel):
    financial_health_score: float | None = None
    
    risk_level: RiskLevel | None = None
    
    confidence_score: float | None = None
    
    credit_decision: CreditDecision

    suggested_loan_amount: float

    loan_limit_min: float

    loan_limit_max: float

    monitoring_frequency: MonitoringFrequency

    risk_grade: str


class AssessmentResponse(AppBaseModel):
    request_id: str | None = None

    status: AssessmentStatus

    summary: AssessmentSummary

    component_scores: list[ComponentScore] = Field(
        default_factory=list
    )

    component_breakdown: list[ComponentBreakdown] = Field(
    default_factory=list,
    )

    positive_signals: list[str] = Field(
        default_factory=list
    )

    negative_signals: list[str] = Field(
        default_factory=list
    )

    warnings: list[str] = Field(
        default_factory=list
    )

    recommendations: list[str] = Field(
    default_factory=list,
    )

    simulation_inputs: SimulationInputs | None = None

    llm_analysis: LLMAnalysis | None = None

    