from fastapi import APIRouter

from backend.app.config import config
from .routes.auth import router as auth_router
from .routes.balconies import router as balcony_router
from .routes.conditions import router as condition_router
from .routes.districts import router as district_router
from .routes.estate import router as estate_router
from .routes.floors import router as floors_router
from .routes.rooms import router as rooms_router
from .routes.storeys import router as storey_router
from .routes.types import router as type_router
from .routes.objects import router as objects_router
from .routes.telegram import router as telegram_router

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
router.include_router(estate_router)
router.include_router(auth_router)
router.include_router(objects_router)
router.include_router(telegram_router)