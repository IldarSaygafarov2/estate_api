from .base import BaseRepo

from infrastructure.database.models import District

from sqlalchemy import (
    select,
    update,
    delete,
    insert
)


class DistrictRepo(BaseRepo):
    async def create_district(self, label: str):
        stmt = (
            insert(District)
            .values(label=label)
            .returning(District)
        )
        result = await self.session.execute(stmt)
        await self.session.commit()
        return result.scalar_one()

    async def delete_district(self, district_id: int):
        stmt = (
            delete(District)
            .where(District.id == district_id)
        )
        await self.session.execute(stmt)
        await self.session.commit()

    async def update_district(self, district_id: int, label: str):
        stmt = (
            update(District)
            .values(label=label)
            .where(District.id == district_id)
            .returning(District)
        )
        result = await self.session.execute(stmt)
        await self.session.commit()
        return result.scalar_one()

    async def get_districts(self):
        stmt = select(District)
        result = await self.session.execute(stmt)
        return result.scalars().all()
