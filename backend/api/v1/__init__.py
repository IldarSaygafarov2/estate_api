from fastapi import APIRouter

from backend.app.config import config
from .routes.balconies import router as balcony_router
from .routes.conditions import router as condition_router
from .routes.districts import router as district_router
from .routes.floors import router as floors_router
from .routes.rooms import router as rooms_router
from .routes.storeys import router as storey_router
from .routes.types import router as type_router

router = APIRouter(
    prefix=config.api_prefix.v1.prefix
)

router.include_router(balcony_router)
router.include_router(condition_router)
router.include_router(district_router)
router.include_router(floors_router)
router.include_router(rooms_router)
router.include_router(storey_router)
router.include_router(type_router)