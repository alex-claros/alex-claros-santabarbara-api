from domain.use_cases.maple.update_maple_use_case import UpdateMapleUseCase
from infrastructure.persistence.repositories.maple_repository_impl import MapleRepositoryImpl

class UpdateMapleUseCaseImpl(UpdateMapleUseCase):
    def __init__(self, maple_repository: MapleRepositoryImpl):
        self.maple_repository = maple_repository

    def execute(self, maple_id: str, updated_data: dict):
        maple = self.maple_repository.find_by_id(maple_id)
        
        for key, value in updated_data.items():
            setattr(maple, key, value)
        
        self.maple_repository.update(maple)
        
        return {"message": f"Maple con ID {maple_id} actualizado exitosamente."}
    
    def execute(self, maple_id: str, updated_data: dict):
        success = self.maple_repository.update(maple_id, updated_data)
        if not success:
            raise ValueError(f"Incubadora con ID {maple_id} no encontrada.")
        
        updated_maple = self.maple_repository.find_by_id(maple_id)
        if not updated_maple:
            raise ValueError(f"No se pudo recuperar la incubadora con ID {maple_id}.")
        
        return updated_maple