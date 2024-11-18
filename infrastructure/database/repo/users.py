from sqlalchemy import (
    select,
    exists, insert
)

from infrastructure.database.models import User
from .base import BaseRepo


class UserRepo(BaseRepo):
    async def is_user_exists(self, username: str):
        query = select(exists().where(User.username == username))
        result = await self.session.execute(query)
        return result.scalar()

    async def get_by_username(
            self,
            username: str
    ):
        query = (
            select(User)
            .where(User.username == username)
        )
        result = await self.session.execute(query)
        return result.scalar_one_or_none()

    async def add_user(self, username: str, password: str):
        query = (
            insert(User)
            .values(username=username, hashed_password=password)
            .returning(User)
        )
        result = await self.session.execute(query)
        return result.scalar_one()

    async def get_by_username_and_password(self, username: str, password: str):
        query = (
            select(User)
            .where(User.username == username)
            .where(User.hashed_password == password)
        )
        result = await self.session.execute(query)
        return result.scalar_one_or_none()