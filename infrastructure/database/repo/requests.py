from dataclasses import dataclass
from sqlalchemy.ext.asyncio import AsyncSession
from .balcony import BalconyRepo


@dataclass
class RequestsRepo:
    session: AsyncSession
    
    @property
    def balcony(self) -> BalconyRepo:
        return BalconyRepo(self.session)

    