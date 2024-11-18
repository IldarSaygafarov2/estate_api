from environs import Env
from sqlalchemy.ext.asyncio import AsyncSession

from infrastructure.database.repo.requests import RequestsRepo


async def add_user(session: AsyncSession):
    env = Env()
    env.read_env('.env')
    repo = RequestsRepo(session)
    if not await repo.user.is_user_exists(username=env.str('USERNAME')):
        await repo.user.add_user(
            username=env.str('USERNAME'),
            password=env.str('PASSWORD'),
        )
        await session.commit()
