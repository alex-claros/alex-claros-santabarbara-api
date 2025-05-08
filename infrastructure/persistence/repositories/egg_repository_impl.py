from typing import List
from domain.models.egg_model import Egg
from domain.repositories.egg_repository import EggRepository
from infrastructure.entities.egg_entity import EggEntity

class EggRepositoryImpl(EggRepository):
    def save(self, egg: Egg):
        entity = EggEntity.from_domain_model(egg)
        entity.save()

    def find_all(self) -> List[Egg]:
            entities = EggEntity.objects()
            return [entity.to_domain_model() for entity in entities]
    
    def find_by_id(self, egg_id: str) -> Egg:
        entity = EggEntity.objects(id=egg_id).first()
        if not entity:
            raise ValueError(f"Incubadora con ID {egg_id} no encontrada.")
        
        return entity.to_domain_model()