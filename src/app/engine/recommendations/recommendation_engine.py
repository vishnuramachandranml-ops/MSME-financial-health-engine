from __future__ import annotations

from app.engine.models.assessment_result import AssessmentResult


class RecommendationEngine:
    """
    Generates business recommendations from the assessment.
    """

    @staticmethod
    def generate(
        result: AssessmentResult,
    ) -> list[str]:

        recommendations: list[str] = []

        negatives = {
            signal.lower()
            for signal in result.negative_signals
        }

        if any("operating expenses" in s for s in negatives):
            recommendations.append(
                "Reduce operating expenses to improve profitability."
            )

        if any("collection period" in s for s in negatives):
            recommendations.append(
                "Improve receivable collection efficiency to strengthen cash flow."
            )

        if any("working capital" in s for s in negatives):
            recommendations.append(
                "Increase working capital to improve short-term liquidity."
            )

        if any("gst filing" in s for s in negatives):
            recommendations.append(
                "Maintain consistent GST filings to improve compliance."
            )

        if any("digital payment" in s for s in negatives):
            recommendations.append(
                "Increase digital payment adoption to strengthen transaction history."
            )

        if any("electricity" in s for s in negatives):
            recommendations.append(
                "Stabilize operational activity to reduce business volatility."
            )

        if any(
            "current assets" in s
            or "working capital" in s
            or "short-term liabilities" in s
            for s in negatives
        ):
            recommendations.append(
                "Strengthen working capital by improving current assets or reducing short-term liabilities."
            )

        return recommendations