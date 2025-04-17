from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from infrastructure.persistence.incubator import (
    initialize_incubator_table,
    create_incubator,
    get_incubator_by_id,
    get_all_incubators,
    update_incubator,
    delete_incubator
)

router = APIRouter(
    prefix="/incubators",
    tags=["Incubadoras"]
)

initialize_incubator_table()

class IncubatorCreate(BaseModel):
    location: str
    capacity: int
    temperature: float
    humidity: float

class IncubatorUpdate(BaseModel):
    location: str
    capacity: int
    temperature: float
    humidity: float

class Incubator(BaseModel):
    id: int
    location: str
    capacity: int
    temperature: float
    humidity: float

@router.post("/", response_model=Incubator)
def create_new_incubator(incubator: IncubatorCreate):
    incubator_id = create_incubator(
        incubator.location, incubator.capacity, incubator.temperature, incubator.humidity
    )
    new_incubator = get_incubator_by_id(incubator_id)
    if not new_incubator:
        raise HTTPException(status_code=500, detail="Error al crear la incubadora")
    return new_incubator

@router.get("/", response_model=list[Incubator])
def list_incubators():
    return get_all_incubators()

@router.get("/{incubator_id}", response_model=Incubator)
def read_incubator(incubator_id: int):
    incubator = get_incubator_by_id(incubator_id)
    if not incubator:
        raise HTTPException(status_code=404, detail="Incubadora no encontrada")
    return incubator

@router.put("/{incubator_id}", response_model=Incubator)
def update_incubator_endpoint(incubator_id: int, incubator: IncubatorUpdate):
    updated = update_incubator(
        incubator_id, incubator.location, incubator.capacity, incubator.temperature, incubator.humidity
    )
    if not updated:
        raise HTTPException(status_code=404, detail="Incubadora no encontrada")
    return get_incubator_by_id(incubator_id)

@router.delete("/{incubator_id}")
def delete_incubator_endpoint(incubator_id: int):
    deleted = delete_incubator(incubator_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Incubadora no encontrada")
    return {"detail": "Incubadora eliminada exitosamente"}
