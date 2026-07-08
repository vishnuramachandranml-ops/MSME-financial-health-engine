from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar

InputType = TypeVar("InputType")
OutputType = TypeVar("OutputType")


class BaseFeatureEngineer(ABC, Generic[InputType, OutputType]):
    """
    Converts validated input models into engine feature models.
    """

    @abstractmethod
    def transform(self, data: InputType) -> OutputType:
        """
        Transform input model into derived feature model.
        """
        raise NotImplementedError