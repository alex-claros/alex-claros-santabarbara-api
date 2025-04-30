from datetime import datetime
from typing import List
from domain.repositories.incubator_repository import IncubatorRepository
from domain.models.incubator_model import Incubator
from infrastructure.entities.incubator_entity import IncubatorEntity

class IncubatorRepositoryImpl(IncubatorRepository):
    def save(self, incubator: Incubator):
        entity = IncubatorEntity.from_domain_model(incubator)
        entity.save()

    def find_all(self) -> List[Incubator]:
            # entities = IncubatorEntity.objects.all()
            entities = IncubatorEntity.objects(is_deleted=False)
            return [entity.to_domain_model() for entity in entities]
    
    def find_by_id(self, incubator_id: str) -> Incubator:
        entity = IncubatorEntity.objects(id=incubator_id).first()
        if not entity:
            raise ValueError(f"Incubadora con ID {incubator_id} no encontrada.")
        
        return entity.to_domain_model()

    def update(self, incubator_id: str, updated_data: dict) -> bool:
        entity = IncubatorEntity.objects(id=incubator_id).first()
        if not entity:
            return False
        
        entity.update(**updated_data)
        return True

    def soft_delete(self, incubator_id: str) -> bool:
        """
        Realiza un soft-delete de una incubadora.
        """
        entity = IncubatorEntity.objects(id=incubator_id).first()
        if not entity:
            return False
        
        entity.update(
            is_deleted=True,
            deleted_at=datetime.now()
        )
        return True

    def find_maples_in_incubator(self, incubator_id: str) -> List:
        """Lista todos los maples en una incubadora específica."""
        entity = IncubatorEntity.objects(id=incubator_id).first()
        if not entity:
            raise ValueError(f"Incubadora con ID {incubator_id} no encontrada.")
        return [m.to_domain_model() for m in entity.maples]