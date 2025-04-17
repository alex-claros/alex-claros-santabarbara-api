from sqlalchemy import Column, String, Integer, Boolean, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class EggEntity(Base):
    __tablename__ = "eggs"

    id = Column(String, primary_key=True)
    position = Column(Integer)  # Posición dentro del maple
    viability = Column(Boolean)
    image_data = Column(String)  # Almacenar la imagen como base64 o referencia
    colorimetry = Column(Float)
    structural_defects = Column(Boolean)
    maple_id = Column(String)  # ID del maple al que pertenece