from abc import ABC, abstractmethod
from domain.models.egg_model import Egg

class CreateEggUseCase(ABC):
    @abstractmethod
    def execute(self, egg: Egg):
        """Crea un nuevo huevo."""
        pass