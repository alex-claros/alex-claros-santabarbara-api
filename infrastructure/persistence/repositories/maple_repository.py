from sqlalchemy.orm import sessionmaker
from domain.repositories.maple_repository import MapleRepository as IMapleRepository
from infrastructure.entities.maple import MapleEntity

class SqlAlchemyMapleRepository(IMapleRepository):
    def __init__(self, session: sessionmaker):
        self.session = session

    def save(self, maple):
        entity = MapleEntity(
            id=maple.id,
            incubator_id=maple.incubator_id
        )
        self.session.add(entity)
        self.session.commit()

    def find_by_id(self, maple_id: str):
        entity = self.session.query(MapleEntity).filter_by(id=maple_id).first()
        if entity:
            return entity.to_domain_model()
        return None

    def find_all(self):
        entities = self.session.query(MapleEntity).all()
        return [entity.to_domain_model() for entity in entities]