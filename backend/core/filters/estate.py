from fastapi import Query
from dataclasses import dataclass
from typing import Optional


@dataclass
class EstateFilter:
    balcony_id: Optional[int] = Query(None)
    district_id: Optional[int] = Query(None)
    room_id: Optional[int] = Query(None)
    type_id: Optional[int] = Query(None)
    floor_id: Optional[int] = Query(None)
    storey_id: Optional[int] = Query(None)
    condition_id: Optional[int] = Query(None)

    name: Optional[str] = Query(None)
    price: Optional[str] = Query(None)

