from abc import ABC, abstractmethod
from domain.models.maple_model import Maple

class CreateMapleUseCase(ABC):
    @abstractmethod
    def execute(self, maple: Maple):
        """
        Crea un nuevo maple en el sistema.
        """
        pass