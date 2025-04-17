from domain.use_cases.base_use_case import BaseUseCase
from domain.repositories.incubator_repository import IncubatorRepository
from domain.repositories.maple_repository import MapleRepository
from domain.repositories.egg_repository import EggRepository

class ListNonViableEggsInIncubatorUseCase(BaseUseCase):
    def __init__(self, incubator_repository: IncubatorRepository, maple_repository: MapleRepository, egg_repository: EggRepository):
        self.incubator_repository = incubator_repository
        self.maple_repository = maple_repository
        self.egg_repository = egg_repository

    def execute(self, incubator_id: str):
        # Verificar que la incubadora exista
        incubator = self.incubator_repository.find_by_id(incubator_id)
        if not incubator:
            raise ValueError("Incubadora no encontrada")
        
        # Obtener todos los maples en la incubadora
        maples = self.maple_repository.find_all()
        non_viable_eggs = []
        
        for maple in maples:
            eggs = self.egg_repository.find_eggs_in_maple(maple.id)
            non_viable_eggs.extend([egg for egg in eggs if not egg.viability])
        
        return {"incubator_id": incubator_id, "non_viable_eggs": [egg.id for egg in non_viable_eggs]}