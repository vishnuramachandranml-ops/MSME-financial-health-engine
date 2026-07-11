from __future__ import annotations

import json

from google import genai

from app.core.settings import settings
from app.llm.models import LLMAnalysis


class GeminiClient:

    MODEL = "gemini-flash-latest"    

    def __init__(self):

        self.client = genai.Client(
            api_key=settings.gemini_api_key,
        )

    def generate(
        self,
        prompt: str,
    ) -> LLMAnalysis:

        response = self.client.models.generate_content(
            model=self.MODEL,
            contents=prompt,
        )

        text = response.text.strip()

        if text.startswith("```"):

            lines = text.splitlines()

            text = "\n".join(
                line
                for line in lines
                if not line.startswith("```")
            )

        return LLMAnalysis.model_validate(
            json.loads(text)
        )