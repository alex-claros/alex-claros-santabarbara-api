from abc import ABC, abstractmethod

class ListEggsInMapleUseCase(ABC):
    @abstractmethod
    def execute(self, maple_id: str):
        """
        Lista todos los huevos asociados a un maple específico.
        """
        pass