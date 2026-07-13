from __future__ import annotations

from app.models.base import AppBaseModel
from app.models.assessment_request import AssessmentRequest
from app.models.simulation_inputs import SimulationInputs


class WhatIfRequest(AppBaseModel):

    original_request: AssessmentRequest

    scenario: SimulationInputs