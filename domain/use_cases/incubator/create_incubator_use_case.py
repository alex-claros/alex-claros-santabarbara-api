from abc import ABC, abstractmethod
from domain.models.incubator_model import Incubator

class CreateIncubatorUseCase(ABC):
    @abstractmethod
    def execute(self, incubator: Incubator):
        """Crea una nueva incubadora."""
        pass