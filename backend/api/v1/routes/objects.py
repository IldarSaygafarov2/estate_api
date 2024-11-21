from fastapi import APIRouter, Depends
from backend.app.config import config
from backend.core.interfaces.objects import ObjectDTO
from backend.core.interfaces.balcony import BalconyDTO
from backend.core.interfaces.condition import ConditionDTO
from backend.core.interfaces.type import TypeDTO
from backend.core.interfaces.room import RoomDTO
from backend.core.interfaces.floor import FloorDTO
from backend.core.interfaces.storey import StoreyDTO
from backend.core.interfaces.district import DistrictDTO



from backend.app.dependencies import get_repo
from typing import Annotated
from infrastructure.database.repo.requests import RequestsRepo
from fastapi.responses import JSONResponse

router = APIRouter(
    prefix=config.api_prefix.v1.objects,
    tags=['Objects']
)


@router.get('/')
async def get_objects(
    repo: Annotated[RequestsRepo, Depends(get_repo)]
) -> ObjectDTO:
    balconies = [BalconyDTO.model_validate(balcony, from_attributes=True) for balcony in await repo.balcony.get_balconies()]
    conditions = [ConditionDTO.model_validate(condition, from_attributes=True) for condition in await repo.condition.get_conditions()]
    types = [TypeDTO.model_validate(type_obj, from_attributes=True) for type_obj in await repo.type.get_all()]
    rooms = [RoomDTO.model_validate(room, from_attributes=True) for room in await repo.room.get_all()]
    floors = [FloorDTO.model_validate(floor, from_attributes=True) for floor in await repo.floor.get_all()]
    districts = [DistrictDTO.model_validate(district, from_attributes=True) for district in await repo.district.get_districts()]
    storeys = [StoreyDTO.model_validate(storey, from_attributes=True) for storey in await repo.storey.get_all()]

    obj = ObjectDTO(
        balconies=balconies,
        conditions=conditions,
        types=types,
        rooms=rooms,
        floors=floors,
        districts=districts,
        storeys=storeys
    )

    return ObjectDTO.model_validate(obj, from_attributes=True)