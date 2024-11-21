from pydantic import BaseModel

from .balcony import BalconyDTO
from .condition import ConditionDTO
from .district import DistrictDTO
from .floor import FloorDTO
from .room import RoomDTO
from .storey import StoreyDTO
from .type import TypeDTO



class ObjectDTO(BaseModel):
    

    balconies: list["BalconyDTO"]
    conditions: list["ConditionDTO"]
    districts: list["DistrictDTO"]
    floors: list["FloorDTO"]
    rooms: list["RoomDTO"]
    storeys: list["StoreyDTO"]
    types: list["TypeDTO"]

