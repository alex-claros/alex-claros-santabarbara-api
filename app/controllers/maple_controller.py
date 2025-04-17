from fastapi import HTTPException
from domain.use_cases.add_egg_to_maple_use_case import AddEggToMapleUseCase
from domain.use_cases.find_eggs_in_maple_use_case import FindEggsInMapleUseCase
from infrastructure.persistence.repositories.maple_repository import SqlAlchemyMapleRepository
from infrastructure.persistence.repositories.egg_repository import SqlAlchemyEggRepository
from sqlalchemy.orm import sessionmaker

class MapleController:
    def __init__(self, session: sessionmaker):
        self.session = session

    def add_egg_to_maple(self, egg_id: str, maple_id: str, position: int):

        egg_repository = SqlAlchemyEggRepository(self.session)
        maple_repository = SqlAlchemyMapleRepository(self.session)
        
        use_case = AddEggToMapleUseCase(egg_repository, maple_repository)
        
        try:
            result = use_case.execute(egg_id, maple_id, position)
            return result
        except ValueError as e:
            raise HTTPException(status_code=404, detail=str(e))

    def find_eggs_in_maple(self, maple_id: str):

        maple_repository = SqlAlchemyMapleRepository(self.session)
        egg_repository = SqlAlchemyEggRepository(self.session)
        
        use_case = FindEggsInMapleUseCase(maple_repository, egg_repository)
        
        try:
            eggs = use_case.execute(maple_id)
            return {"maple_id": maple_id, "eggs": [egg.id for egg in eggs]}
        except ValueError as e:
            raise HTTPException(status_code=404, detail=str(e))