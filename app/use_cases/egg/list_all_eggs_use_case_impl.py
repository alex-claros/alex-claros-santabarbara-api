from typing import List
from domain.use_cases.egg.list_all_eggs_use_case import ListAllEggsUseCase
from infrastructure.persistence.repositories.egg_repository_impl import EggRepositoryImpl
from domain.models.egg_model import Egg

class ListAllEggsUseCaseImpl(ListAllEggsUseCase):
    def __init__(self, egg_repository: EggRepositoryImpl):
        self.egg_repository = egg_repository

    def execute(self) -> List[Egg]:
        return self.egg_repository.find_all()