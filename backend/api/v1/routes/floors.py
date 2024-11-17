from fastapi import APIRouter

from backend.app.config import config


router = APIRouter(
    prefix=config.api_prefix.v1.floors,
    tags=['Floors']
)

@router.post('/')
async def create_floor():
    return ''


@router.delete('/{id}')
async def delete_floor(id: int):
    return ''

