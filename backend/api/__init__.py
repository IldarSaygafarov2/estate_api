from fastapi import APIRouter

from backend.api.v1 import router as v1_router

from backend.app.config import config


router = APIRouter(
    prefix=config.api_prefix.prefix
)

router.include_router(v1_router)
