from typing import List
from domain.use_cases.incubator.list_non_viable_eggs_incubator_use_case import ListNonViableEggsUseCase
from infrastructure.persistence.repositories.incubator_repository_impl import IncubatorRepositoryImpl
from domain.models.egg_model import Egg

class ListNonViableEggsUseCaseImpl(ListNonViableEggsUseCase):
    def __init__(self, incubator_repository: IncubatorRepositoryImpl):
        self.incubator_repository = incubator_repository

    def execute(self, incubator_id: str) -> List[Egg]:
        incubator = self.incubator_repository.find_by_id(incubator_id)
        if not incubator:
            raise ValueError(f"Incubadora con ID {incubator_id} no encontrada.")
        
        non_viable_eggs = []
        for maple in incubator.maples:
            for egg in maple.eggs:
                if not egg.viability:
                    non_viable_eggs.append(egg)
        
        return non_viable_eggs