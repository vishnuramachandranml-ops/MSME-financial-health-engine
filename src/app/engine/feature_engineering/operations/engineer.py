from __future__ import annotations

from app.engine.feature_engineering.operations.calculator import (
    OperationsCalculator,
)
from app.engine.interfaces.base_feature_engineer import (
    BaseFeatureEngineer,
)
from app.engine.models.operations_features import (
    OperationsFeatures,
)
from app.models.operations import Operations


class OperationsFeatureEngineer(
    BaseFeatureEngineer[
        Operations,
        OperationsFeatures,
    ]
):
    """
    Generates derived operational features from raw business
    operational data.
    """

    def transform(
        self,
        data: Operations,
    ) -> OperationsFeatures:
        """
        Transform raw operational data into derived features.
        """

        return OperationsCalculator.calculate(data)