from typing import Optional

from pydantic import BaseModel, Field


class EstateFilter(BaseModel):
    condition: Optional[str] = Field(None)
    district: Optional[str] = Field(None)
    rooms: Optional[str] = Field(None)
    type: Optional[str] = Field(None)
    price_min: Optional[int] = Field(None)
    price_max: Optional[int] = Field(None)
