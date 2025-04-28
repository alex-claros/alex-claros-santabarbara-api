from abc import ABC, abstractmethod
from domain.models.incubator_model import Incubator

class SoftDeleteIncubatorUseCase(ABC):
    @abstractmethod
    def execute(self, incubator: Incubator):
        """
        Realiza un soft-delete de una incubadora.
        """
        pass