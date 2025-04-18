from fastapi import APIRouter, Depends, File, UploadFile
from app.controllers.egg_controller import EggController
from core.database import get_db_session

router = APIRouter()

@router.post("/add-egg-to-maple/")
def add_egg_to_maple(
    egg_id: str,
    maple_id: str,
    position: int,
    image: UploadFile = File(...),
    session=Depends(get_db_session)
):
    controller = EggController(session)
    
    with open(f"temp_{image.filename}", "wb") as f:
        f.write(image.file.read())
    
    result = controller.add_egg_to_maple(egg_id, maple_id, position, f"temp_{image.filename}")
    return result