from datetime import datetime
from typing import List, Optional
import uuid
from domain.models.egg_model import Egg

class Maple:
    def __init__(
        self,
        name: str,
        capacity: int,
        status: str,
        level: str,
        id: str = None,
        eggs: Optional[List[Egg]] = None,
        load_date: datetime = None,
        responsible: str = None,
        is_deleted: bool = False, 
        deleted_at: datetime = None

    ):
        """
        Representa un maple en el dominio del negocio.
        
        """
        self.id = id if id else str(uuid.uuid4())
        self.name = name
        self.capacity = capacity
        self.status = status
        self.level = level
        self.eggs = eggs or []
        self.load_date = load_date
        self.responsible = responsible
        self.is_deleted = is_deleted
        self.deleted_at = deleted_at

    def to_dict(self):
        """
        Convierte el objeto de dominio en un diccionario.
        """
        return {
            "id": self.id,
            "name": self.name,
            "capacity": self.capacity,
            "status": self.status,
            "level": self.level,
            "eggs": [e.to_dict() for e in self.eggs],
            "load_date": self.load_date,
            "responsible": self.responsible,
            "is_deleted": self.is_deleted,
            "deleted_at": self.deleted_at
        }