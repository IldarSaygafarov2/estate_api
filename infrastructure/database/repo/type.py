from .base import BaseRepo
from sqlalchemy import (
    select,
    update,
    insert,
    delete
)

from infrastructure.database.models import Type

class TypeRepo(BaseRepo):
    async def create(self, label: str):
        stmt = (
            insert(Type)
            .values(label=label)
            .returning(Type)
        )
        result = await self.session.execute(stmt)
        await self.session.commit()
        return result.scalar_one()

    async def update(self, type_id: int, label: str):
        stmt = (
            update(Type)
            .values(label=label)
            .where(Type.id == type_id)
            .returning(Type)
        )
        result = await self.session.execute(stmt)
        await self.session.commit()
        return result.scalar_one()

    async def delete(self, type_id: int):
        stmt = (
            delete(Type)
            .where(Type.id == type_id)
        )
        await self.session.execute(stmt)
        await self.session.commit()

    async def get_all(self):
        stmt = select(Type)
        result = await self.session.execute(stmt)
        return result.scalars().all()
