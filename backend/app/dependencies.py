from backend.app.config import config
from backend.core.services.jwt_service import JwtService
from backend.core.services.password_service import PasswordService
from infrastructure.database.repo.requests import RequestsRepo
from infrastructure.database.setup import (
    create_engine,
    create_session_pool
)

engine = create_engine(config.db)
session_pool = create_session_pool(engine)


async def get_repo():
    async with session_pool() as session:
        yield RequestsRepo(session)


def get_password_service() -> PasswordService:
    return PasswordService()


def get_jwt_service() -> JwtService:
    return JwtService(
        secret_key=config.access_token.token_secret,
        algorithm=config.access_token.algorith,
        expire_time=config.access_token.token_expire_seconds
    )

