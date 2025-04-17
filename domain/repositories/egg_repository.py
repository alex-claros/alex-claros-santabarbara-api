from abc import ABC, abstractmethod
from typing import List
from domain.models.egg_model import Egg

class EggRepository(ABC):
    @abstractmethod
    def save(self, egg: Egg):
        """Guarda un huevo en el repositorio."""
        pass

    @abstractmethod
    def find_by_id(self, egg_id: str) -> Egg:
        """Busca un huevo por su ID."""
        pass

    @abstractmethod
    def find_all(self) -> List[Egg]:
        """Lista todos los huevos."""
        pass

    @abstractmethod
    def find_non_viable_eggs(self) -> List[Egg]:
        """Lista todos los huevos no viables."""
        pass