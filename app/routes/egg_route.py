from fastapi import APIRouter, Depends
from app.controllers.egg_controller import EggController
from sqlalchemy.orm import sessionmaker

router = APIRouter()

@router.post("/detect-viability/")
def detect_viability(egg_id: str, session: sessionmaker = Depends(get_db_session)):
    controller = EggController(session)
    return controller.detect_viability(egg_id)

@router.post("/add-egg-to-maple/")
def add_egg_to_maple(egg_id: str, maple_id: str, position: int, session: sessionmaker = Depends(get_db_session)):
    controller = EggController(session)
    return controller.add_egg_to_maple(egg_id, maple_id, position)