from typing import List
from fastapi import APIRouter, Depends, HTTPException
from app.controllers.incubator_controller import IncubatorController
from infrastructure.schemas.incubator_schema import IncubatorSchema  # Modelo Pydantic para Incubator
from domain.models.maple_model import Maple
from domain.models.incubator_model import Incubator        

router = APIRouter()

controller = IncubatorController()

@router.get("/incubators/", response_model=List[IncubatorSchema])
def list_incubators():
    try:
        incubators = controller.list_all_incubators()
        return incubators
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/incubators/", response_model=IncubatorSchema)
def create_incubator(incubator: IncubatorSchema):
    try:
        incubator_domain = Incubator(
            id=incubator.id,
            name=incubator.name,
            capacity=incubator.capacity,
            status=incubator.status,
            temperature=incubator.temperature,
            last_mant=incubator.last_mant
        )
        result = controller.create_incubator(incubator_domain)
        return result
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.put("/incubators/{incubator_id}", response_model=IncubatorSchema)
def update_incubator(incubator_id: str, updated_data: dict):
    """
    Actualiza una incubadora existente.
    """
    try:
        # Llama al controlador para actualizar la incubadora
        incubator_domain = controller.update_incubator(incubator_id, updated_data)
        # Retorna el resultado como un modelo Pydantic
        return IncubatorSchema(**incubator_domain.__dict__)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.delete("/incubators/{incubator_id}")
def delete_incubator(incubator_id: str):
    """
    Elimina una incubadora.
    """
    try:
        # Llama al controlador para eliminar la incubadora
        return controller.delete_incubator(incubator_id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/incubators/{incubator_id}/add-maple/", response_model=IncubatorSchema)
def add_maple_to_incubator(incubator_id: str, maple: Maple):
    """
    Agrega un maple a una incubadora.
    """
    try:
        # Convierte el modelo Pydantic a tu modelo de dominio
        incubator_domain = controller.add_maple_to_incubator(incubator_id, maple)
        # Retorna el resultado como un modelo Pydantic
        return IncubatorSchema(**incubator_domain.__dict__)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/incubators/{incubator_id}/non-viable-eggs/")
def list_non_viable_eggs(incubator_id: str):
    """
    Lista los huevos no viables de una incubadora.
    """
    try:
        # Llama al controlador para listar los huevos no viables
        return controller.list_non_viable_eggs(incubator_id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))