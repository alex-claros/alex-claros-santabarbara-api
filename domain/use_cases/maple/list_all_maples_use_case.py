from abc import ABC, abstractmethod
from typing import List
from domain.models.maple_model import Maple

class ListAllMaplesUseCase(ABC):
    @abstractmethod
    def execute(self) -> List[Maple]:
        """
        Lista todos los maples activos en el sistema.
        """
        pass