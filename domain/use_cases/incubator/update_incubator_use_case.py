from abc import ABC, abstractmethod
from domain.models.incubator_model import Incubator

class UpdateIncubatorUseCase(ABC):
    @abstractmethod
    def execute(self, incubator: Incubator):
        """Actualiza una incubadora existente."""
        pass