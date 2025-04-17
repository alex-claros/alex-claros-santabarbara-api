from abc import ABC, abstractmethod
from typing import List
from domain.models.maple_model import Maple

class MapleRepository(ABC):
    @abstractmethod
    def save(self, maple: Maple):
        """Guarda un maple en el repositorio."""
        pass

    @abstractmethod
    def find_by_id(self, maple_id: str) -> Maple:
        """Busca un maple por su ID."""
        pass

    @abstractmethod
    def find_all(self) -> List[Maple]:
        """Lista todos los maples."""
        pass

    @abstractmethod
    def find_eggs_in_maple(self, maple_id: str) -> List:
        """Lista todos los huevos en un maple específico."""
        pass