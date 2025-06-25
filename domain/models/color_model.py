import uuid
from datetime import datetime

class Color:
    def __init__(self, r: int, g: int, b: int):
        self.r = r
        self.g = g
        self.b = b

    def to_dict(self):
        return {"r": self.r, "g": self.g, "b": self.b}