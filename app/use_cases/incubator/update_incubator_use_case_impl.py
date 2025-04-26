from domain.use_cases.incubator.update_incubator_use_case import UpdateIncubatorUseCase
from infrastructure.persistence.repositories.incubator_repository_impl import IncubatorRepositoryImpl

class UpdateIncubatorUseCaseImpl(UpdateIncubatorUseCase):
    def __init__(self, incubator_repository: IncubatorRepositoryImpl):
        self.incubator_repository = incubator_repository

    def execute(self, incubator_id: str, updated_data: dict):
        success = self.incubator_repository.update(incubator_id, updated_data)
        if not success:
            raise ValueError(f"Incubadora con ID {incubator_id} no encontrada.")
        
        updated_incubator = self.incubator_repository.find_by_id(incubator_id)
        if not updated_incubator:
            raise ValueError(f"No se pudo recuperar la incubadora con ID {incubator_id}.")
        
        return updated_incubator