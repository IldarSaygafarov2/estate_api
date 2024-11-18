from datetime import datetime
from typing import Optional

from fastapi import UploadFile

from pydantic import BaseModel


class EstateImageDTO(BaseModel):
    id: int
    url: str
    created_at: datetime
    updated_at: datetime


class EstateDTO(BaseModel):
    id: int
    name: str
    description: str
    price: str
    owner_phone: str
    realtor_phone: str
    created_at: datetime
    updated_at: datetime

    balcony_id: int
    condition_id: int
    district_id: int
    type_id: int
    room_id: int
    storey_id: int
    images: list[EstateImageDTO]


class EstateCreateDTO(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[str] = None
    owner_phone: Optional[str] = None
    realtor_phone: Optional[str] = None

    balcony_id: Optional[int] = None
    condition_id: Optional[int] = None
    district_id: Optional[int] = None
    type_id: Optional[int] = None
    room_id: Optional[int] = None
    storey_id: Optional[int] = None
