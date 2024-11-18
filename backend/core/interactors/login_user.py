from backend.core.interfaces.user import LoginUserDTO
from backend.core.services.jwt_service import JwtService
from infrastructure.database.repo.requests import RequestsRepo


class LoginUserInteractor:
    def __init__(self, request_repo: RequestsRepo, jwt_service: JwtService):
        self.request_repo = request_repo
        self.jwt_service = jwt_service

    async def __call__(self, login_user: LoginUserDTO):
        user = await self.request_repo.user.get_by_username_and_password(username=login_user.username,
                                                                         password=login_user.password)
        if not user:
            raise ValueError('invalid username or password')

        access_token = self.jwt_service.create_access_token({'sub': login_user.username})
        return access_token
