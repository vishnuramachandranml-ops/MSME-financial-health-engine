from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from app.engine.models.assessment_result import AssessmentResult

FeatureType = TypeVar("FeatureType")


class BaseAssessor(ABC, Generic[FeatureType]):
    """
    Base class for all assessors.
    """

    @abstractmethod
    def assess(self, features: FeatureType) -> AssessmentResult:
        """
        Assess a business dimension.
        """
        raise NotImplementedError