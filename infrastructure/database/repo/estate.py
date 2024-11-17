from .base import BaseRepo

from sqlalchemy import (
    insert
)

from infrastructure.database.models import Estate


class EstateRepo(BaseRepo):
    async def create(
            self,
            name: str,
            description: str,
            price: str,
            owner_phone: str,
            realtor_phone: str,
            balcony_id: int,
            condition_id: int,
            district_id: int,
            type_id: int,
            room_id: int,
            storey_id: int
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
            )
            .returning(Estate)
        )
        result = await self.session.execute(stmt)
        await self.session.commit()
        return result.scalar_one()
