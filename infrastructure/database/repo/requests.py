from dataclasses import dataclass
from sqlalchemy.ext.asyncio import AsyncSession
from .balcony import BalconyRepo
from .condition import ConditionRepo


@dataclass
class RequestsRepo:
    session: AsyncSession
    
    @property
    def balcony(self) -> BalconyRepo:
        return BalconyRepo(self.session)

    @property
    def condition(self) -> ConditionRepo:
        return ConditionRepo(self.session)
    