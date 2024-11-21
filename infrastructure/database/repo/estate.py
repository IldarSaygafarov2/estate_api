from sqlalchemy import delete, insert, select, update
from sqlalchemy.orm import selectinload

from infrastructure.database.models import Estate

from .base import BaseRepo


class EstateRepo(BaseRepo):
    async def get_all(self):
        stmt = (
            select(Estate)
            .options(
                selectinload(Estate.images),

                selectinload(Estate.balcony),
                selectinload(Estate.condition),
                selectinload(Estate.type),
                selectinload(Estate.floor),
                selectinload(Estate.storey),
                selectinload(Estate.room),
                selectinload(Estate.district),
            )
        )
        result = await self.session.execute(stmt)
        return result.scalars().all()

    async def create(
            self,
            name: str,
            description: str,
            price: str,
            owner_phone: str,
            realtor_phone: str,
            manager_phone: str,
            notes: str,
            balcony_id: int,
            condition_id: int,
            district_id: int,
            type_id: int,
            room_id: int,
            storey_id: int,
            floor_id: int
    ):
        stmt = (
            insert(Estate)
            .values(
                name=name,
                description=description,
                price=price,
                owner_phone=owner_phone,
                realtor_phone=realtor_phone,
                balcony_id=balcony_id,
                condition_id=condition_id,
                district_id=district_id,
                type_id=type_id,
                room_id=room_id,
                storey_id=storey_id,
                floor_id=floor_id,
                manager_phone=manager_phone,
                notes=notes,
            )
            .returning(Estate)
        )
        result = await self.session.execute(stmt)
        await self.session.commit()
        return result.scalar_one()

    async def get_by_id(self, estate_id: int):
        stmt = (
            select(Estate)
            .where(Estate.id == estate_id)
            .options(selectinload(Estate.images))
        )
        result = await self.session.execute(stmt)
        return result.scalar_one()

    async def delete(self, estate_id: int):
        stmt = (
            delete(Estate)
            .where(Estate.id == estate_id)
        )
        await self.session.execute(stmt)
        await self.session.commit()

    async def update(
            self,
            estate_id: int,
            **kwargs
    ):
        stmt = (
            update(Estate)
            .values(
                **kwargs
            )
            .where(Estate.id == estate_id)
            .options(selectinload(Estate.images))
            .returning(Estate)
        )
        result = await self.session.execute(stmt)
        await self.session.commit()
        return result.scalar_one()