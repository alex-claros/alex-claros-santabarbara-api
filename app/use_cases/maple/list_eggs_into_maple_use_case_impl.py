from domain.use_cases.maple.list_eggs_into_maple_use_case import ListEggsInMapleUseCase
from infrastructure.persistence.repositories.maple_repository_impl import MapleRepositoryImpl

class ListEggsInMapleUseCaseImpl(ListEggsInMapleUseCase):
    def __init__(self, maple_repository: MapleRepositoryImpl):
        self.maple_repository = maple_repository

    def execute(self, maple_id: str):
        eggs = self.maple_repository.find_eggs_in_maple(maple_id)
        
        return [egg.to_dict() for egg in eggs]