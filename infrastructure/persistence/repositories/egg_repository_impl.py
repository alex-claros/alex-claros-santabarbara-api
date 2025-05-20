from typing import List
from domain.repositories.egg_repository import EggRepository
from domain.models.egg_model import Egg
from infrastructure.entities.egg_entity import EggEntity

class EggRepositoryImpl(EggRepository):
    def save(self, egg: Egg):
        entity = EggEntity.from_domain_model(egg)
        entity.save()

    def find_all(self) -> List[Egg]:
        entities = EggEntity.objects()
        return [entity.to_domain_model() for entity in entities]

    def find_by_maple_id(self, maple_id: str) -> List[Egg]:
        entities = EggEntity.objects(maple_id=maple_id)
        return [entity.to_domain_model() for entity in entities]

    def find_non_viable_eggs(self) -> List[Egg]:
        entities = EggEntity.objects(viability=False)
        return [entity.to_domain_model() for entity in entities]