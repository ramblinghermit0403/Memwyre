from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class MemoryBase(BaseModel):
    title: str
    content: str

class MemoryCreate(MemoryBase):
    pass

class MemoryUpdate(MemoryBase):
    pass

from typing import Union

class MemoryInDBBase(MemoryBase):
    id: Union[int, str]
    user_id: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    type: str = "memory"

    class Config:
        from_attributes = True

class Memory(MemoryInDBBase):
    pass
