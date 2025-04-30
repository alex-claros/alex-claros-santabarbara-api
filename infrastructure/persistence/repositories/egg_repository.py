from sqlalchemy.orm import sessionmaker
from domain.repositories.egg_repository import EggRepository as IEggRepository
from infrastructure.entities.egg_entity import EggEntity

class SqlAlchemyEggRepository(IEggRepository):
    def __init__(self, session: sessionmaker):
        self.session = session

    def save(self, egg):
        entity = EggEntity(
            id=egg.id,
            position=egg.position,
            viability=egg.viability,
            image_url=egg.image_url,
            colorimetry=egg.colorimetry,
            structural_defects=egg.structural_defects
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