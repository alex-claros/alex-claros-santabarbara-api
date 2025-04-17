from fastapi import APIRouter, Depends
from app.controllers.maple_controller import MapleController
from sqlalchemy.orm import sessionmaker

router = APIRouter()

@router.post("/add-egg/")
def add_egg_to_maple(egg_id: str, maple_id: str, position: int, session: sessionmaker = Depends(get_db_session)):
    controller = MapleController(session)
    return controller.add_egg_to_maple(egg_id, maple_id, position)

@router.get("/eggs-in-maple/")
def find_eggs_in_maple(maple_id: str, session: sessionmaker = Depends(get_db_session)):
    controller = MapleController(session)
    return controller.find_eggs_in_maple(maple_id)