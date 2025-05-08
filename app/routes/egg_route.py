from fastapi import APIRouter, Depends, HTTPException
from app.controllers.egg_controller import EggController
from domain.models.egg_model import Egg
from infrastructure.schemas.egg_schema import EggSchema
from pydantic import BaseModel

router = APIRouter()

controller = EggController()

@router.post("/eggs/", response_model=dict)
def create_egg(egg_data: EggSchema):
    try:
        result = controller.create_egg(egg_data.dict())
        return {"message": "Egg created successfully", "data": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/eggs/", response_model=list)
def list_eggs():
    try:
        eggs = controller.list_eggs()
        return eggs
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
