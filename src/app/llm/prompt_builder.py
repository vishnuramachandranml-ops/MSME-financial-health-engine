from __future__ import annotations

from app.engine.models.assessment_result import AssessmentResult


class PromptBuilder:

    @staticmethod
    def build(
        result: AssessmentResult,
        risk_level: str,
        recommendations: list[str],
    ) -> str:

        components = "\n".join(
            f"- {component.name}: {component.score:.2f}"
            for component in result.component_scores
        )

        positives = "\n".join(
            f"- {signal}"
            for signal in result.positive_signals
        )

        negatives = "\n".join(
            f"- {signal}"
            for signal in result.negative_signals
        )
        recommendations_text = "\n".join(
            f"- {recommendation}"
            for recommendation in recommendations
        )

        return f"""
You are a Senior Credit Underwriter at a commercial bank.

A deterministic financial assessment engine has already generated the scores.

Never modify the score.

Never modify the risk level.

Never invent information.

Use ONLY the supplied assessment.

Financial Health Score:
{result.component.score:.2f}

Risk Level:
{risk_level}

Component Scores:
{components}

Positive Signals:
{positives}

Negative Signals:
{negatives}

Recommendations:
{recommendations_text}

Return ONLY valid JSON.

{{
    "executive_summary":"",
    "credit_opinion":"",
    "monitoring_points":[]
}}

Requirements:

- Executive Summary <=120 words.
- Credit Opinion <=40 words.
- Maximum 5 monitoring points.
- Professional banking language.
"""