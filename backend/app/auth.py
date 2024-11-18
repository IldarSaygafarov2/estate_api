from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer

from backend.app.dependencies import get_jwt_service, get_repo
from backend.core.services.jwt_service import JwtService
from infrastructure.database.models import User
from infrastructure.database.repo.requests import RequestsRepo

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='/api/v1/auth/login')


async def get_current_user(
        token: str = Depends(oauth2_scheme),
        jwt_service: JwtService = Depends(get_jwt_service),
        repo: RequestsRepo = Depends(get_repo)
) -> User:
    try:
        payload = jwt_service.decode_token(token)
        username: str = payload.get('sub')
        if username is None:
            raise HTTPException(status_code=401, detail='Invalid token')

        user = await repo.user.get_by_username(username=username)
        if not user:
            raise HTTPException(status_code=404, detail='User not found')

        return user
    except:
        raise HTTPException(status_code=401, detail='Invalid token')
