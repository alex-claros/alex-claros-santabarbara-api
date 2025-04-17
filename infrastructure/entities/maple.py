from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class MapleEntity(Base):
    __tablename__ = "maples"

    id = Column(String, primary_key=True)
    incubator_id = Column(String)