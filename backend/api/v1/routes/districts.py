from fastapi import APIRouter

from backend.app.config import config

router = APIRouter(
    prefix=config.api_prefix.v1.districts,
    tags=['Districts']
)

@router.post('/')
async def create_district():
    return ''

@router.delete('/{id}')
async def delete_district(id: int):
    return ''

