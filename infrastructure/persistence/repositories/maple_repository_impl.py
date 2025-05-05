from datetime import datetime
from typing import List
from domain.models.maple_model import Maple
from domain.repositories.maple_repository import MapleRepository
from infrastructure.entities.maple_entity import MapleEntity

class MapleRepositoryImpl(MapleRepository):
    def save(self, maple: Maple):
        entity = MapleEntity.from_domain_model(maple)
        entity.save()

    def find_all(self) -> List[Maple]:
        entities = MapleEntity.objects(is_deleted=False)
        return [entity.to_domain_model() for entity in entities]
    
    def find_by_id(self, maple_id: str) -> Maple:
        entity = MapleEntity.objects(id=maple_id).first()
        if not entity:
            raise ValueError(f"Maple con ID {maple_id} no encontrado.")
        return entity.to_domain_model()
    
    def update(self, maple_id: str, updated_data: dict) -> bool:
        entity = MapleEntity.objects(id=maple_id).first()
        if not entity:
            return False
        
        entity.update(**updated_data)
        return True

    def soft_delete(self, maple_id: str):
        entity = MapleEntity.objects(id=maple_id).first()
        if not entity:
            raise ValueError(f"Maple con ID {maple_id} no encontrado.")
        
        entity.update(
            is_deleted=True,
            deleted_at=datetime.now()
        )

    def find_eggs_in_maple(self, maple_id: str) -> List:
        """
        Lista todos los huevos en un maple específico.
        """
        entity = MapleEntity.objects(id=maple_id).first()
        if not entity:
            raise ValueError(f"Maple con ID {maple_id} no encontrado.")
        
        return [e.to_domain_model() for e in entity.eggs]