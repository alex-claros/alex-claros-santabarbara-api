from domain.models.maple_model import Maple
from abc import ABC, abstractmethod

class SoftDeleteMapleUseCase(ABC):
    @abstractmethod
    def execute(self, maple: Maple):
        """
        Realiza un soft-delete de un maple.
        """
        pass