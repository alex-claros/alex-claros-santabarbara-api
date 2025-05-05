from domain.use_cases.maple.create_maple_use_case import CreateMapleUseCase
from infrastructure.persistence.repositories.maple_repository_impl import MapleRepositoryImpl
from domain.models.maple_model import Maple

class CreateMapleUseCaseImpl(CreateMapleUseCase):
    def __init__(self, maple_repository: MapleRepositoryImpl):
        self.maple_repository = maple_repository

    def execute(self, maple: Maple):
        self.maple_repository.save(maple)
        
        return {
            "id": maple.id,
            "name": maple.name,
            "capacity": maple.capacity,
            "status": maple.status,
            "level": maple.level,
            "eggs": [],
            "load_date": maple.load_date,
            "responsible": maple.responsible,
            "is_deleted": maple.is_deleted,
            "deleted_at": maple.deleted_at
        }