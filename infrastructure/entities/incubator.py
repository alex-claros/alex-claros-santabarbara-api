from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class IncubatorEntity(Base):
    __tablename__ = "incubators"

    id = Column(String, primary_key=True)
    capacity = Column(Integer)  # Capacidad máxima de maples