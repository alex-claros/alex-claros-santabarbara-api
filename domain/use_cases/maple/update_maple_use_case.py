from domain.models.maple_model import Maple
from abc import ABC, abstractmethod

class UpdateMapleUseCase(ABC):
    @abstractmethod
    def execute(self, maple: Maple):
        """
        Actualiza un maple existente en el sistema.
        """
        pass