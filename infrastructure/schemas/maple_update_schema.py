from datetime import datetime
from pydantic import BaseModel
from typing import Optional

class MapleUpdateSchema(BaseModel):
    name: Optional[str] = None
    capacity: Optional[int] = None
    status: Optional[str] = None
    level: Optional[str] = None
    eggs: Optional[list] = None
    load_date: Optional[datetime] = None
    responsible: Optional[str] = None 
    is_deleted: Optional[bool] = None
    deleted_at: Optional[datetime] = None

    class Config:
        from_attributes = True