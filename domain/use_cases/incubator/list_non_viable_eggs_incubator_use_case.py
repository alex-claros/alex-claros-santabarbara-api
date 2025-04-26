from abc import ABC, abstractmethod
from typing import List
from domain.models.egg_model import Egg

class ListNonViableEggsUseCase(ABC):
    @abstractmethod
    def execute(self, incubator_id: str) -> List[Egg]:
        """Lista todos los huevos no viables en una incubadora específica."""
        pass