from abc import ABC, abstractmethod
from typing import List
from domain.models.incubator_model import Incubator

class ListAllIncubatorsUseCase(ABC):
    @abstractmethod
    def execute(self) -> List[Incubator]:
        pass