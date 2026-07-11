from __future__ import annotations

from app.engine.feature_engineering.alternate_data.calculator import (
    AlternateDataCalculator,
)
from app.engine.interfaces.base_feature_engineer import (
    BaseFeatureEngineer,
)
from app.engine.models.alternate_data_features import (
    AlternateDataFeatures,
)
from app.models.alternate_data import AlternateData


class AlternateDataFeatureEngineer(
    BaseFeatureEngineer[
        AlternateData,
        AlternateDataFeatures,
    ]
):
    """
    Generates derived alternate-data features.
    """

    def transform(
        self,
        data: AlternateData,
    ) -> AlternateDataFeatures:

        return AlternateDataCalculator.calculate(data)