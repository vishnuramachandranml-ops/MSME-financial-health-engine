from __future__ import annotations

import logging

from app.engine.models.assessment_result import AssessmentResult
from app.llm.gemini_client import GeminiClient
from app.llm.models import LLMAnalysis
from app.llm.prompt_builder import PromptBuilder

logger = logging.getLogger(__name__)


class SummaryService:

    def __init__(self):

        self.client = GeminiClient()

    def summarize(
        self,
        result: AssessmentResult,
        risk_level: str,
        recommendations: list[str],
    )-> LLMAnalysis | None:

        prompt = PromptBuilder.build(
            result=result,
            risk_level=risk_level,
            recommendations=recommendations,
        )

        try:

            return self.client.generate(
                prompt
            )

        except Exception:

            logger.exception(
                "Gemini summary generation failed."
            )

            return None