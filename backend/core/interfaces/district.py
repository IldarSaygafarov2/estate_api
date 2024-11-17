from datetime import datetime

from pydantic import BaseModel


class DistrictDTO(BaseModel):
    id: int
    label: str
    created_at: datetime
    updated_at: datetime


class DistrictCreateDTO(BaseModel):
    label: str

