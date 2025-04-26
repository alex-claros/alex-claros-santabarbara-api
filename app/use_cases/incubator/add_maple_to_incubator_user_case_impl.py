from typing import Any
from domain.use_cases.incubator.add_maple_to_incubator_use_case import AddMapleToIncubatorUseCase
from infrastructure.persistence.repositories.incubator_repository_impl import IncubatorRepositoryImpl

class AddMapleToIncubatorUseCaseImpl(AddMapleToIncubatorUseCase):
    def __init__(self, incubator_repository: IncubatorRepositoryImpl):
        self.incubator_repository = incubator_repository

    def execute(self, incubator_id: str, maple: Any):
        incubator = self.incubator_repository.find_by_id(incubator_id)
        if not incubator:
            raise ValueError(f"Incubadora con ID {incubator_id} no encontrada.")
        
        if len(incubator.maples) >= incubator.capacity:
            raise ValueError("La incubadora ha alcanzado su capacidad máxima de maples.")
        
        incubator.maples.append(maple)
        self.incubator_repository.save(incubator)
        return incubator