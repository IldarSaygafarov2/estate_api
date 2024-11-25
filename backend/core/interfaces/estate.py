import json
from datetime import datetime
from typing import Optional

from pydantic import BaseModel, model_validator

# from .balcony import BalconyDTO
# from .condition import ConditionDTO
# from .district import DistrictDTO
# from .floor import FloorDTO
# from .room import RoomDTO
# from .storey import StoreyDTO
# from .type import TypeDTO


class EstateImageDTO(BaseModel):
    id: int
    url: str
    created_at: datetime
    updated_at: datetime


class EstateDTO(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[str] = None
    owner_phone: Optional[str] = None
    realtor_phone: Optional[str] = None
    manager_phone: Optional[str] = None
    notes: Optional[str] = None
    created_at: datetime
    updated_at: datetime

    balcony: Optional[str] = None
    condition: Optional[str] = None
    district: Optional[str] = None
    type: Optional[str] = None
    room: Optional[str] = None
    storey: Optional[str] = None
    floor: Optional[str] = None
    
    images: Optional[list[EstateImageDTO]]


class EstateCreateDTO(BaseModel):
    name: str
    price: str
    description: Optional[str] = None
    owner_phone: Optional[str] = None
    realtor_phone: Optional[str] = None
    manager_phone: Optional[str] = None
    notes: Optional[str] = None

    balcony: str
    condition: str
    district: str
    type: str
    room: str
    storey: str
    floor: str

    @model_validator(mode='before')
    @classmethod
    def validate_to_json(cls, value):
        if isinstance(value, str):
            return cls(**json.loads(value))
        return value


class EstateUpdateDTO(BaseModel):
    name: Optional[str] = None
    price: Optional[str] = None
    description: Optional[str] = None
    owner_phone: Optional[str] = None
    realtor_phone: Optional[str] = None
    manager_phone: Optional[str] = None
    notes: Optional[str] = None

    balcony: str
    condition: str
    district: str
    type: str
    room: str
    storey: str
    floor: str

    @model_validator(mode='before')
    @classmethod
    def validate_to_json(cls, value):
        if isinstance(value, str):
            return cls(**json.loads(value))
        return value