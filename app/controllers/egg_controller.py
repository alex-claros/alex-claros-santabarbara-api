from app.services.roboflow_service import RoboflowService
from app.use_cases.egg.create_egg_use_case_impl import CreateEggUseCaseImpl
from app.use_cases.egg.list_all_eggs_use_case_impl import ListAllEggsUseCaseImpl
from infrastructure.persistence.repositories.egg_repository_impl import EggRepositoryImpl

class EggController:
    def __init__(self):
        self.repository = EggRepositoryImpl()
        self.roboflow_service = RoboflowService()
        self.create_egg_use_case = CreateEggUseCaseImpl(self.repository, self.roboflow_service)
        self.list_eggs_use_case = ListAllEggsUseCaseImpl(self.repository)

    def create_egg(self, image_content: bytes):
        return self.create_egg_use_case.execute(image_content)

    def list_eggs(self):
        return self.list_eggs_use_case.execute()
