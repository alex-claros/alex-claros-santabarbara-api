from datetime import datetime
from typing import List, Optional
import uuid
from domain.models.maple_model import Maple

class Incubator:
    def __init__(
        self,
        name: str,
        capacity: int,
        status: str,
        temperature: str,
        last_mant: str,
        id: str = None,
        maples: Optional[List[Maple]] = None,
        is_deleted: bool = False, 
        deleted_at: datetime = None

    ):
        """
        Representa una incubadora en el dominio del negocio.

        :param id: ID único de la incubadora.
        :param name: Nombre reconocible de la incubadora.
        :param capacity: Capacidad máxima de maples.
        :param status: Estado actual de la incubadora (funcionamiento, disponible, etc.).
        :param temperature: Temperatura ideal de la incubadora.
        :param last_mant: Última vez que se realizó mantenimiento.
        :param maples: Lista de maples asociados a la incubadora.
        """
        self.id = id if id else str(uuid.uuid4())
        self.name = name
        self.capacity = capacity
        self.status = status
        self.temperature = temperature
        self.last_mant = last_mant
        self.maples = maples or []
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
            "temperature": self.temperature,
            "last_mant": self.last_mant,
            "maples": [m.to_dict() for m in self.maples],
            "is_deleted": self.is_deleted,
            "deleted_at": self.deleted_at
        }