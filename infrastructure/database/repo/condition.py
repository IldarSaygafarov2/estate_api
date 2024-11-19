from sqlalchemy import (
    insert,
    select,
    update, delete
)

from infrastructure.database.models import Condition
from .base import BaseRepo


class ConditionRepo(BaseRepo):
    async def create_condition(self, label: str):
        stmt = (
            insert(Condition)
            .values(label=label)
            .returning(Condition)
        )

        result = await self.session.execute(stmt)
        await self.session.commit()
        return result.scalar_one()

    async def get_conditions(self):
        stmt = (
            select(Condition)
        )
        result = await self.session.execute(stmt)
        return result.scalars().all()

    async def get_condition(self, condition_id: int):
        stmt = (
            select(Condition)
            .where(Condition.id == condition_id)
        )
        result = await self.session.execute(stmt)
        return result.scalar_one()

    async def update_condition(self, condition_id: int, label: str):
        stmt = (
            update(Condition)
            .values(label=label)
            .where(Condition.id == condition_id)
            .returning(Condition)
        )
        result = await self.session.execute(stmt)
        await self.session.commit()
        return result.scalar_one()

    async def delete_condition(self, condition_id: int):
        stmt = (
            delete(Condition)
            .where(Condition.id == condition_id)
        )
        await self.session.execute(stmt)
        await self.session.commit()