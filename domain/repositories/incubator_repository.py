from abc import ABC, abstractmethod
from typing import List
from domain.models.incubator_model import Incubator

class IncubatorRepository(ABC):
    @abstractmethod
    def save(self, incubator: Incubator):
        """Guarda una incubadora en el repositorio."""
        pass

    @abstractmethod
    def find_all(self) -> List[Incubator]:
        """Lista todas las incubadoras."""
        pass

    @abstractmethod
    def update(self, incubator: Incubator):
        """Actualiza una incubadora existente."""
        pass

    @abstractmethod
    def find_by_id(self, incubator_id: str) -> Incubator:
        """Busca una incubadora por su ID."""
        pass

    @abstractmethod
    def delete(self, incubator_id: str):
        """Elimina una incubadora por su ID."""
        pass

    @abstractmethod
    def find_maples_in_incubator(self, incubator_id: str) -> List:
        """Lista todos los maples en una incubadora específica."""
        pass