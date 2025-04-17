from domain.repositories.incubator_repository import IncubatorRepository
from infrastructure.entities.incubator import IncubatorEntity
from sqlalchemy.orm import sessionmaker
from typing import List
from domain.models.incubator_model import Incubator

class SqlAlchemyIncubatorRepository(IncubatorRepository):
    def __init__(self, session: sessionmaker):
        self.session = session

    def save(self, incubator: Incubator):
        entity = IncubatorEntity(
            id=incubator.id,
            capacity=incubator.capacity
        )
        self.session.add(entity)
        self.session.commit()

    def find_by_id(self, incubator_id: str):
        entity = self.session.query(IncubatorEntity).filter_by(id=incubator_id).first()
        if entity:
            return entity.to_domain_model()
        return None

    def find_all(self) -> List[Incubator]:
        entities = self.session.query(IncubatorEntity).all()
        return [entity.to_domain_model() for entity in entities]

    def find_maples_in_incubator(self, incubator_id: str):
        entity = self.session.query(IncubatorEntity).filter_by(id=incubator_id).first()
        if entity:
            return [maple.to_domain_model() for maple in entity.maples]
        return []