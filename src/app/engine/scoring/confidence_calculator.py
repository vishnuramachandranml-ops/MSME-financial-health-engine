class ConfidenceCalculator:

    @staticmethod
    def from_metric_availability(
        available: int,
        expected: int,
    ) -> float:

        if expected == 0:
            return 0

        return round((available / expected) * 100, 2)