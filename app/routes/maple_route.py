from typing import List
from fastapi import APIRouter, Depends, HTTPException
from app.controllers.maple_controller import MapleController
from infrastructure.schemas.maple_schema import MapleSchema
from infrastructure.schemas.maple_update_schema import MapleUpdateSchema
from infrastructure.schemas.egg_schema import EggSchema
from domain.models.maple_model import Maple
from domain.models.egg_model import Egg

router = APIRouter()

controller = MapleController()

@router.get("/maple/", response_model=List[MapleSchema])
def list_all_maples():
    try:
        result = controller.list_all_maples()
        return result
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/maple/", response_model=MapleSchema)
def create_maple(maple: MapleSchema):
    try:
        maple_domain = Maple(
            id=maple.id,
            name=maple.name,
            capacity=maple.capacity,
            status=maple.status,
            level=maple.level,
            load_date=maple.load_date,
            responsible=maple.responsible,
            is_deleted=maple.is_deleted,
            deleted_at=maple.deleted_at
        )
        result = controller.create_maple(maple_domain)
        return result
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.put("maple/{maple_id}", response_model=MapleSchema)
def update_maple(maple_id: str, updated_data: MapleUpdateSchema):
    
    try:
        maple_domain = controller.update_maple(maple_id, updated_data.dict(exclude_unset=True))
        maple_dict = maple_domain.to_dict()
        
        return MapleSchema(**maple_dict)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.delete("maple/{maple_id}", response_model=MapleUpdateSchema)
def soft_delete_maple(maple_id: str):
    try:
        result = controller.soft_delete_maple(maple_id)
        return result
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

# @router.get("/{maple_id}", response_model=MapleSchema)
# def list_maple_by_id(maple_id: str):
#     """
#     Obtiene un maple por su ID.
#     """
#     try:
#         result = controller.get_maple_by_id(maple_id)
#         return result
#     except ValueError as e:
#         raise HTTPException(status_code=404, detail=str(e))

# @router.post("/{maple_id}/eggs", response_model=EggSchema)
# def add_egg_to_maple(maple_id: str, egg: EggSchema):
#     """
#     Asocia un huevo a un maple específico.
#     """
#     try:
#         # Convierte el modelo Pydantic a tu modelo de dominio
#         egg_domain = Egg(
#             id=egg.id,
#             size=egg.size,
#             texture=egg.texture,
#             color=egg.color,
#             anomalies=egg.anomalies,
#             image_url=egg.image_url,
#             viability=egg.viability,
#             confidence_score=egg.confidence_score
#         )
#         result = controller.add_egg_to_maple(maple_id, egg_domain.to_dict())
#         return result
#     except ValueError as e:
#         raise HTTPException(status_code=400, detail=str(e))

# @router.get("/{maple_id}/eggs", response_model=List[EggSchema])
# def list_eggs_in_maple(maple_id: str):
#     """
#     Lista todos los huevos asociados a un maple específico.
#     """
#     try:
#         result = controller.list_eggs_in_maple(maple_id)
#         return result
#     except ValueError as e:
#         raise HTTPException(status_code=404, detail=str(e))