from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from domain.entities.incubator import Incubator
from domain.entities.egg import Egg

@dataclass
class Maple:
    id: int
    location: str
    description: str = ""
    incubator: Optional[Incubator] = None
    eggs: List[Egg] = field(default_factory=list)

    def assign_incubator(self, incubator: Incubator):
        """Asigna la incubadora a este maple."""
        self.incubator = incubator

    def add_egg(self, egg: Egg):
        """Agrega un huevo a este maple y establece la asociación."""
        egg.assign_maple(self)
        self.eggs.append(egg)
