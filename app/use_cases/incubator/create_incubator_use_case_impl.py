from domain.use_cases.incubator.create_incubator_use_case import CreateIncubatorUseCase
from infrastructure.persistence.repositories.incubator_repository_impl import IncubatorRepositoryImpl
from domain.models.incubator_model import Incubator

class CreateIncubatorUseCaseImpl(CreateIncubatorUseCase):
    def __init__(self, incubator_repository: IncubatorRepositoryImpl):
        self.incubator_repository = incubator_repository

    def execute(self, incubator: Incubator):
        self.incubator_repository.save(incubator)
        
        return {
            "id": incubator.id,
            "name": incubator.name,
            "capacity": incubator.capacity,
            "status": incubator.status,
            "temperature": incubator.temperature,
            "last_mant": incubator.last_mant,
            "maples": [],
            "is_deleted": incubator.is_deleted,
            "deleted_at": incubator.deleted_at

        }