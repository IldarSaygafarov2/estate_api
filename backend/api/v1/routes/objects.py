from fastapi import APIRouter, Depends
from backend.app.config import config
from backend.core.interfaces.objects import ObjectDTO
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
    balconies = await repo.balcony.get_balconies()
    conditions = await repo.condition.get_conditions()
    types = await repo.type.get_all()
    rooms = await repo.room.get_all()
    floors = await repo.floor.get_all()
    districts = await repo.district.get_districts()
    storeys = await repo.storey.get_all()

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