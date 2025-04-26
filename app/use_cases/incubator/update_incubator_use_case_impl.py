from domain.use_cases.incubator.update_incubator_use_case import UpdateIncubatorUseCase
from infrastructure.persistence.repositories.incubator_repository_impl import IncubatorRepositoryImpl

class UpdateIncubatorUseCaseImpl(UpdateIncubatorUseCase):
    def __init__(self, incubator_repository: IncubatorRepositoryImpl):
        self.incubator_repository = incubator_repository

    def execute(self, incubator):
        success = self.incubator_repository.update(incubator)
        if not success:
            raise ValueError(f"Incubadora con ID {incubator.id} no encontrada.")
        return {"message": "Incubadora actualizada exitosamente"}