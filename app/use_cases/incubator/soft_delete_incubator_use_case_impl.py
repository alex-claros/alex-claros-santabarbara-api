from datetime import datetime
from domain.use_cases.incubator.soft_delete_incubator_use_case import SoftDeleteIncubatorUseCase
from infrastructure.persistence.repositories.incubator_repository_impl import IncubatorRepositoryImpl

class SoftDeleteIncubatorUseCaseImpl(SoftDeleteIncubatorUseCase):
    def __init__(self, incubator_repository: IncubatorRepositoryImpl):
        self.incubator_repository = incubator_repository

    def execute(self, incubator_id: str):
        success = self.incubator_repository.soft_delete(incubator_id)
        if not success:
            raise ValueError(f"Incubadora con ID {incubator_id} no encontrada.")
        
        deleted_incubator = self.incubator_repository.find_by_id(incubator_id)
        if not deleted_incubator:
            raise ValueError(f"No se pudo recuperar la incubadora con ID {incubator_id}.")
        
        return deleted_incubator