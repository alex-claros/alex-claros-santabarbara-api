from domain.repositories.egg_repository import EggRepository
from infrastructure.entities.egg import EggEntity
from sqlalchemy.orm import sessionmaker
from domain.models.egg_model import Egg

class SqlAlchemyEggRepository(EggRepository):
    def __init__(self, session: sessionmaker):
        self.session = session

    def save(self, egg: Egg):
        entity = EggEntity(
            id=egg.id,
            position=egg.position,
            viability=egg.viability,
            image_data=egg.image_data,
            colorimetry=egg.colorimetry,
            structural_defects=egg.structural_defects,
            maple_id=egg.maple_id
        )
        self.session.add(entity)
        self.session.commit()

    def find_by_id(self, egg_id: str):
        entity = self.session.query(EggEntity).filter_by(id=egg_id).first()
        if entity:
            return entity.to_domain_model()
        return None

    def find_all(self):
        entities = self.session.query(EggEntity).all()
        return [entity.to_domain_model() for entity in entities]

    def find_non_viable_eggs(self):
        entities = self.session.query(EggEntity).filter_by(viability=False).all()
        return [entity.to_domain_model() for entity in entities]