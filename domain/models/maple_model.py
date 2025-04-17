from typing import List, Optional
from pydantic import BaseModel
from domain.models.egg_model import Egg

class Maple(BaseModel):
    id: str
    incubator_id: str  # ID de la incubadora a la que pertenece
    eggs: List[Egg] = []  # Lista de huevos en el maple

    def add_egg(self, egg: Egg, position: int):
        """Añade un huevo al maple en una posición específica."""
        if any(e.position == position for e in self.eggs):
            raise ValueError(f"Ya existe un huevo en la posición {position}.")
        egg.position = position
        self.eggs.append(egg)

    def get_egg_by_position(self, position: int) -> Optional[Egg]:
        """Obtiene un huevo por su posición."""
        for egg in self.eggs:
            if egg.position == position:
                return egg
        return None