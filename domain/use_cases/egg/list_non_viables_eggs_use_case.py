from abc import ABC, abstractmethod
from typing import List
from domain.models.egg_model import Egg

class ListNonViableEggsUseCase(ABC):
    @abstractmethod
    def execute(self, Egg) -> List[Egg]:
        """Lista todos los huevos no viables."""
        pass