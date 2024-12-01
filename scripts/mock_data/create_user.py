from environs import Env
from sqlalchemy.ext.asyncio import AsyncSession

from infrastructure.database.repo.requests import RequestsRepo


async def add_ceo_user(session: AsyncSession):
    env = Env()
    env.read_env(".env")
    repo = RequestsRepo(session)
    if not await repo.user.is_user_exists(username=env.str("CEO_USERNAME")):
        await repo.user.add_user(
            username=env.str("CEO_USERNAME"),
            password=env.str("CEO_PASSWORD"),
            user_type="CEO",
        )
        await session.commit()


async def add_employee_user(session: AsyncSession):
    env = Env()
    env.read_env(".env")
    repo = RequestsRepo(session)

    if not await repo.user.is_user_exists(username=env.str("EMPLOYEE_USERNAME")):
        await repo.user.add_user(
            username=env.str("EMPLOYEE_USERNAME"),
            password=env.str("EMPLOYEE_PASSWORD"),
            user_type="EMPLOYEE",
        )
        await session.commit()
