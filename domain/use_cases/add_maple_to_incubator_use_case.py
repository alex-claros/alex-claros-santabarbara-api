from domain.repositories.incubator_repository import IncubatorRepository
from domain.repositories.maple_repository import MapleRepository

class AddMapleToIncubatorUseCase:
    def __init__(self, incubator_repository: IncubatorRepository, maple_repository: MapleRepository):
        self.incubator_repository = incubator_repository
        self.maple_repository = maple_repository

    def execute(self, maple_id: str, incubator_id: str):
        incubator = self.incubator_repository.find_by_id(incubator_id)
        if not incubator:
            raise ValueError("Incubadora no encontrada")
        
        maple = self.maple_repository.find_by_id(maple_id)
        if not maple:
            raise ValueError("Maple no encontrado")
        
        incubator.add_maple(maple)
        self.incubator_repository.save(incubator)
        
        return {"message": f"Maple {maple_id} añadido a la incubadora {incubator_id}"}