from fastapi import APIRouter, Depends
from app.controllers.incubator_controller import IncubatorController
from sqlalchemy.orm import sessionmaker
from core.database import get_db_session

router = APIRouter()

@router.post("/add-maple/")
def add_maple_to_incubator(maple_id: str, incubator_id: str, session: sessionmaker = Depends(get_db_session)):
    controller = IncubatorController(session)
    return controller.add_maple_to_incubator(maple_id, incubator_id)

@router.get("/non-viable-eggs/")
def list_non_viable_eggs_in_incubator(incubator_id: str, session: sessionmaker = Depends(get_db_session)):
    controller = IncubatorController(session)
    return controller.list_non_viable_eggs_in_incubator(incubator_id)