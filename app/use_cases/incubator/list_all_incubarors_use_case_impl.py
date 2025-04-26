from typing import List
from domain.use_cases.incubator.list_all_incubators_use_case import ListAllIncubatorsUseCase
from infrastructure.persistence.repositories.incubator_repository_impl import IncubatorRepositoryImpl
from domain.models.incubator_model import Incubator

class ListAllIncubatorsUseCaseImpl(ListAllIncubatorsUseCase):
    def __init__(self, incubator_repository: IncubatorRepositoryImpl):
        self.incubator_repository = incubator_repository

    def execute(self) -> List[Incubator]:
        return self.incubator_repository.find_all()