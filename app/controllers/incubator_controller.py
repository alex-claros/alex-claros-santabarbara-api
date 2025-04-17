from fastapi import HTTPException
from domain.use_cases.list_non_viable_eggs_incubator_use_case import ListNonViableEggsInIncubatorUseCase
from domain.use_cases.add_maple_to_incubator_use_case import AddMapleToIncubatorUseCase
from infrastructure.persistence.repositories.incubator_repository import SqlAlchemyIncubatorRepository
from infrastructure.persistence.repositories.maple_repository import SqlAlchemyMapleRepository
from infrastructure.persistence.repositories.egg_repository import SqlAlchemyEggRepository
from sqlalchemy.orm import sessionmaker

class IncubatorController:
    def __init__(self, session: sessionmaker):
        self.session = session

    def add_maple_to_incubator(self, maple_id: str, incubator_id: str):
        incubator_repository = SqlAlchemyIncubatorRepository(self.session)
        maple_repository = SqlAlchemyMapleRepository(self.session)
        use_case = AddMapleToIncubatorUseCase(incubator_repository, maple_repository)
        
        try:
            result = use_case.execute(maple_id, incubator_id)
            return result
        except ValueError as e:
            raise HTTPException(status_code=404, detail=str(e))

    def list_non_viable_eggs_in_incubator(self, incubator_id: str):
        incubator_repository = SqlAlchemyIncubatorRepository(self.session)
        maple_repository = SqlAlchemyMapleRepository(self.session)
        egg_repository = SqlAlchemyEggRepository(self.session)
        use_case = ListNonViableEggsInIncubatorUseCase(incubator_repository, maple_repository, egg_repository)
        
        try:
            non_viable_eggs = use_case.execute(incubator_id)
            return {"incubator_id": incubator_id, "non_viable_eggs": [egg.id for egg in non_viable_eggs]}
        except ValueError as e:
            raise HTTPException(status_code=404, detail=str(e))