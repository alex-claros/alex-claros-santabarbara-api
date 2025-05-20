from typing import List
from fastapi import APIRouter, Depends, File, HTTPException, UploadFile
from app.controllers.egg_controller import EggController
from app.services.roboflow_service import RoboflowService
from domain.models.egg_model import Egg
from infrastructure.persistence.repositories.egg_repository_impl import EggRepositoryImpl
from infrastructure.schemas.egg_schema import EggSchema
from pydantic import BaseModel

router = APIRouter()

controller = EggController()

@router.get("/eggs/", response_model=List[EggSchema])
def list_eggs():
    try:
        eggs = controller.list_eggs()
        return eggs
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.get("/eggs/non-viable/", response_model=List[EggSchema])
def list_non_viable_eggs():
    """
    Lista los huevos no viables.
    """
    try:
        non_viable_eggs = controller.list_non_viable_eggs()
        return non_viable_eggs
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/eggs/process/")
async def process_eggs(
    file: UploadFile = File(...)
):
    """
    Procesa una imagen y guarda los huevos detectados.
    """
    try:
        image_content = await file.read() 
        result = controller.create_egg(image_content)

        return result
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))