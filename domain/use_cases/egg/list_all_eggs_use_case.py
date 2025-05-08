from abc import ABC, abstractmethod
from typing import List
from domain.models.egg_model import Egg

class ListAllEggsUseCase(ABC):
    @abstractmethod
    def execute(self) -> List[Egg]:
        pass