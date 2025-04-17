from abc import ABC, abstractmethod

class BaseUseCase(ABC):
    @abstractmethod
    def execute(self, *args, **kwargs):
        """Ejecuta la lógica del caso de uso."""
        pass