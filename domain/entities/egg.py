from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from domain.entities.viability import ViabilityResult
from domain.entities.maple import Maple

@dataclass
class Egg:
    id: int
    size: str
    color: str
    texture: str
    viability_result: Optional[ViabilityResult] = None
    maple: Optional[Maple] = None

    def assign_viability_result(self, result: ViabilityResult):
        """Asigna el resultado de viabilidad al huevo."""
        self.viability_result = result

    def assign_maple(self, maple: Maple):
        """Asigna el maple al que pertenece este huevo."""
        self.maple = maple
