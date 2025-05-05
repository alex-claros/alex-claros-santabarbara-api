from app.use_cases.maple.create_maple_use_case_impl import CreateMapleUseCaseImpl
from app.use_cases.maple.update_maple_use_case_impl import UpdateMapleUseCaseImpl
from app.use_cases.maple.soft_delete_maple_use_case_impl import SoftDeleteMapleUseCaseImpl
from app.use_cases.maple.list_all_maples_use_case_impl import ListAllMaplesUseCaseImpl
from app.use_cases.maple.list_eggs_into_maple_use_case_impl import ListEggsInMapleUseCaseImpl
from infrastructure.persistence.repositories.maple_repository_impl import MapleRepositoryImpl
from domain.models.maple_model import Maple

class MapleController:
    def __init__(self):
        self.repository = MapleRepositoryImpl()
        self.create_maple_use_case = CreateMapleUseCaseImpl(self.repository)
        self.list_all_maples_use_case = ListAllMaplesUseCaseImpl(self.repository)
        self.update_maple_use_case = UpdateMapleUseCaseImpl(self.repository)
        self.delete_maple_use_case = SoftDeleteMapleUseCaseImpl(self.repository)
        self.list_eggs_in_maple_use_case = ListEggsInMapleUseCaseImpl(self.repository)

    def create_maple(self, maple: Maple):
        return self.create_maple_use_case.execute(maple)
    
    def list_all_maples(self):
        return self.list_all_maples_use_case.execute()

    def update_maple(self, maple_id: str, updated_data: dict):
        return self.update_maple_use_case.execute(maple_id, updated_data)

    def soft_delete_maple(self, maple_id: str):
        return self.delete_maple_use_case.execute(maple_id)

    # def add_egg_to_maple(self, maple_id: str, egg_data: dict):
    #     return self.add_egg_to_maple_use_case.execute(maple_id, egg_data)

    def list_eggs_in_maple(self, maple_id: str):
        return self.list_eggs_in_maple_use_case.execute(maple_id)