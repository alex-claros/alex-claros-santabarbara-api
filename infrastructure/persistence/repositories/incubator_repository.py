from sqlalchemy.orm import sessionmaker
from domain.repositories.incubator_repository import IncubatorRepository as IIncubatorRepository
from infrastructure.entities.incubator import IncubatorEntity

class SqlAlchemyIncubatorRepository(IIncubatorRepository):
    def __init__(self, session: sessionmaker):
        self.session = session

    def save(self, incubator):
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

    def find_all(self):
        entities = self.session.query(IncubatorEntity).all()
        return [entity.to_domain_model() for entity in entities]

    def add_maple(self, incubator_id: str, maple):
        incubator_entity = self.session.query(IncubatorEntity).filter_by(id=incubator_id).first()
        if not incubator_entity:
            raise ValueError(f"Incubadora con ID {incubator_id} no encontrada.")
        
        if len(incubator_entity.maples) >= incubator_entity.capacity:
            raise ValueError("La incubadora ha alcanzado su capacidad máxima de maples.")
        
        incubator_entity.maples.append(maple)
        self.session.commit()
        return incubator_entity.to_domain_model()

    def remove_maple(self, incubator_id: str, maple_id: str):
        incubator_entity = self.session.query(IncubatorEntity).filter_by(id=incubator_id).first()
        if not incubator_entity:
            raise ValueError(f"Incubadora con ID {incubator_id} no encontrada.")
        
        # Filtrar los maples para eliminar el especificado
        incubator_entity.maples = [
            maple for maple in incubator_entity.maples if str(maple.id) != maple_id
        ]
        self.session.commit()
        return incubator_entity.to_domain_model()

    def list_non_viable_eggs(self, incubator_id: str):
        incubator_entity = self.session.query(IncubatorEntity).filter_by(id=incubator_id).first()
        if not incubator_entity:
            raise ValueError(f"Incubadora con ID {incubator_id} no encontrada.")
        
        non_viable_eggs = []
        for maple in incubator_entity.maples:
            for egg in maple.eggs:
                if not egg.viability:
                    non_viable_eggs.append(egg)
        
        return [egg.to_domain_model() for egg in non_viable_eggs]