from dataclasses import dataclass

from sqlalchemy.ext.asyncio import AsyncSession

from .balcony import BalconyRepo
from .condition import ConditionRepo
from .district import DistrictRepo
from .estate import EstateRepo
from .estate_image import EstateImageRepo
from .floor import FloorRepo
from .room import RoomRepo
from .storey import StoreyRepo
from .type import TypeRepo
from .users import UserRepo


@dataclass
class RequestsRepo:
    session: AsyncSession
    
    @property
    def balcony(self) -> BalconyRepo:
        return BalconyRepo(self.session)

    @property
    def condition(self) -> ConditionRepo:
        return ConditionRepo(self.session)

    @property
    def district(self) -> DistrictRepo:
        return DistrictRepo(self.session)

    @property
    def floor(self) -> FloorRepo:
        return FloorRepo(self.session)

    @property
    def room(self) -> RoomRepo:
        return RoomRepo(self.session)

    @property
    def storey(self) -> StoreyRepo:
        return StoreyRepo(self.session)

    @property
    def type(self) -> TypeRepo:
        return TypeRepo(self.session)

    @property
    def estate(self) -> EstateRepo:
        return EstateRepo(self.session)

    @property
    def estate_image(self) -> EstateImageRepo:
        return EstateImageRepo(self.session)

    @property
    def user(self) -> UserRepo:
        return UserRepo(self.session)