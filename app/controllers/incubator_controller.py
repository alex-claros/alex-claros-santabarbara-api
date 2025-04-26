from app.use_cases.incubator.create_incubator_use_case_impl import CreateIncubatorUseCaseImpl
from app.use_cases.incubator.update_incubator_use_case_impl import UpdateIncubatorUseCaseImpl
from app.use_cases.incubator.add_maple_to_incubator_user_case_impl import AddMapleToIncubatorUseCaseImpl
from app.use_cases.incubator.list_non_viable_eggs_incubator_use_case_impl import ListNonViableEggsUseCaseImpl
from app.use_cases.incubator.list_all_incubators_use_case_impl import ListAllIncubatorsUseCaseImpl
from infrastructure.persistence.repositories.incubator_repository_impl import IncubatorRepositoryImpl
from domain.models.incubator_model import Incubator

class IncubatorController:
    def __init__(self):
        self.repository = IncubatorRepositoryImpl()
        self.create_incubator_use_case = CreateIncubatorUseCaseImpl(self.repository)
        self.list_all_incubators_use_case = ListAllIncubatorsUseCaseImpl(self.repository)
        self.update_incubator_use_case = UpdateIncubatorUseCaseImpl(self.repository)
        self.add_maple_use_case = AddMapleToIncubatorUseCaseImpl(self.repository)
        self.list_non_viable_eggs_use_case = ListNonViableEggsUseCaseImpl(self.repository)

    def list_all_incubators(self):
        return self.repository.find_all()

    def create_incubator(self, incubator: Incubator):
        return self.create_incubator_use_case.execute(incubator)

    def update_incubator(self, incubator_id: str, updated_data: dict):
        return self.update_incubator_use_case.execute(incubator_id, updated_data)

    def add_maple_to_incubator(self, incubator_id: str, maple: dict):
        return self.add_maple_use_case.execute(incubator_id, maple)

    def list_non_viable_eggs(self, incubator_id: str):
        return self.list_non_viable_eggs_use_case.execute(incubator_id)