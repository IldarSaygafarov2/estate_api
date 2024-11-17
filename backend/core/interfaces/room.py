from datetime import datetime

from pydantic import BaseModel


class RoomDTO(BaseModel):
    id: int
    label: str
    created_at: datetime
    updated_at: datetime


class RoomCreateDTO(BaseModel):
    label: str