from app.use_cases.egg.egg_analysis_use_case_impl import ImageClassificationUseCaseImpl
from app.use_cases.egg.list_all_eggs_use_case_impl import ListAllEggsUseCaseImpl
from infrastructure.persistence.repositories.egg_repository_impl import EggRepositoryImpl

class EggController:
    def __init__(self):
        self.repository = EggRepositoryImpl()
        self.create_egg_use_case = (self.repository)
        self.list_eggs_use_case = ListAllEggsUseCaseImpl(self.repository)

    def create_egg(self, egg_data: dict):
        return self.create_egg_use_case.execute(egg_data)

    def list_eggs(self):
        return self.list_eggs_use_case.execute()
