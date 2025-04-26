from abc import ABC, abstractmethod
from typing import Any
from domain.models.incubator_model import Incubator

class AddMapleToIncubatorUseCase(ABC):
    @abstractmethod
    def execute(self, incubator_id: str, maple: Any):
        """Añade un maple a una incubadora específica."""
        pass