from typing import List
from domain.use_cases.maple.list_all_maples_use_case import ListAllMaplesUseCase
from infrastructure.persistence.repositories.maple_repository_impl import MapleRepositoryImpl
from domain.models.maple_model import Maple

class ListAllMaplesUseCaseImpl(ListAllMaplesUseCase):
    def __init__(self, maple_repository: MapleRepositoryImpl):
        self.maple_repository = maple_repository

    def execute(self) -> List[Maple]:
        return self.maple_repository.find_all()