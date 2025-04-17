from domain.repositories.maple_repository import MapleRepository
from infrastructure.entities.maple import MapleEntity
from sqlalchemy.orm import sessionmaker
from typing import List
from domain.models.maple_model import Maple

class SqlAlchemyMapleRepository(MapleRepository):
    def __init__(self, session: sessionmaker):
        self.session = session

    def save(self, maple: Maple):
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

    def find_all(self) -> List[Maple]:
        entities = self.session.query(MapleEntity).all()
        return [entity.to_domain_model() for entity in entities]

    def find_eggs_in_maple(self, maple_id: str):
        entity = self.session.query(MapleEntity).filter_by(id=maple_id).first()
        if entity:
            return [egg.to_domain_model() for egg in entity.eggs]
        return []