from domain.use_cases.base_use_case import BaseUseCase
from domain.repositories.maple_repository import MapleRepository
from domain.repositories.egg_repository import EggRepository

class AddEggToMapleUseCase(BaseUseCase):
    def __init__(self, egg_repository: EggRepository, maple_repository: MapleRepository):
        self.egg_repository = egg_repository
        self.maple_repository = maple_repository

    def execute(self, egg_id: str, maple_id: str, position: int):
        # Verificar que el huevo exista
        egg = self.egg_repository.find_by_id(egg_id)
        if not egg:
            raise ValueError("Huevo no encontrado")
        
        # Verificar que el maple exista
        maple = self.maple_repository.find_by_id(maple_id)
        if not maple:
            raise ValueError("Maple no encontrado")
        
        # Añadir el huevo al maple
        maple.add_egg(egg, position)
        self.maple_repository.save(maple)
        
        return {"message": f"Huevo {egg_id} añadido al maple {maple_id} en la posición {position}"}