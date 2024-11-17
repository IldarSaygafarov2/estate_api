from fastapi import APIRouter

from backend.app.config import config


router = APIRouter(
    prefix=config.api_prefix.v1.types,
    tags=['Types']
)


@router.post('/')
async def create_type():
    return ''


@router.delete('/{id}')
async def delete_type(id: int):
    return ''