from domain.repositories.maple_repository import MapleRepository
from domain.repositories.egg_repository import EggRepository

class FindEggsInMapleUseCase:
    def __init__(self, maple_repository: MapleRepository, egg_repository: EggRepository):
        self.maple_repository = maple_repository
        self.egg_repository = egg_repository

    def execute(self, maple_id: str):
        maple = self.maple_repository.find_by_id(maple_id)
        if not maple:
            raise ValueError("Maple no encontrado")
        
        eggs = self.egg_repository.find_eggs_in_maple(maple_id)
        return eggs