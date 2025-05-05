from domain.use_cases.maple.soft_delete_maple_use_case import SoftDeleteMapleUseCase
from infrastructure.persistence.repositories.maple_repository_impl import MapleRepositoryImpl

class SoftDeleteMapleUseCaseImpl(SoftDeleteMapleUseCase):
    def __init__(self, maple_repository: MapleRepositoryImpl):
        self.maple_repository = maple_repository
    
    def execute(self, maple_id: str):
        success = self.maple_repository.soft_delete(maple_id)
        if not success:
            raise ValueError(f"Incubadora con ID {maple_id} no encontrada.")
        
        deleted_maple = self.maple_repository.find_by_id(maple_id)
        if not deleted_maple:
            raise ValueError(f"No se pudo recuperar la incubadora con ID {maple_id}.")
        
        return deleted_maple