from abc import ABC, abstractmethod
from typing import List
from domain.models.egg_model import Egg

class EggRepository(ABC):
    @abstractmethod
    def save(self, egg: Egg):
        pass

    @abstractmethod
    def find_by_maple_id(self, maple_id: str) -> List[Egg]:
        pass

    @abstractmethod
    def find_non_viable_eggs(self) -> List[Egg]:
        pass