from typing import Annotated

from fastapi import APIRouter, Depends

from backend.app.config import config
from backend.app.dependencies import get_repo
from backend.core.interfaces.district import (
    DistrictDTO,
    DistrictCreateDTO
)
from infrastructure.database.repo.requests import RequestsRepo

router = APIRouter(
    prefix=config.api_prefix.v1.districts,
    tags=['Districts']
)


@router.get('/', response_model=list[DistrictDTO])
async def get_districts(
        repo: Annotated[RequestsRepo, Depends(get_repo)],
):
    districts = await repo.district.get_districts()
    return districts


@router.post('/', response_model=DistrictDTO)
async def create_district(
        repo: Annotated[RequestsRepo, Depends(get_repo)],
        district: DistrictCreateDTO
):
    new_district = await repo.district.create_district(label=district.label)
    return DistrictDTO.model_validate(new_district, from_attributes=True)


@router.delete('/{district_id}', status_code=204)
async def delete_district(
        district_id: int,
        repo: Annotated[RequestsRepo, Depends(get_repo)],
):
    await repo.district.delete_district(district_id)


@router.patch('/{district_id}', response_model=DistrictDTO)
async def update_district(
        district_id: int,
        repo: Annotated[RequestsRepo, Depends(get_repo)],
        district: DistrictCreateDTO
):
    updated_district = await repo.district.update_district(district_id=district_id, label=district.label)
    return DistrictDTO.model_validate(updated_district, from_attributes=True)
