from datetime import datetime

from pydantic import BaseModel


class ConditionDTO(BaseModel):
    id: int
    label: str
    created_at: datetime
    updated_at: datetime


class ConditionCreateDTO(BaseModel):
    label: str
