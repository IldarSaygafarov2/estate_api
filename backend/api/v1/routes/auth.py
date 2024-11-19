from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from backend.app.config import config
from backend.app.dependencies import (
    get_jwt_service,
    get_repo
)
from backend.core.interactors.login_user import LoginUserInteractor
from backend.core.interfaces.user import (
    LoginUserDTO
)
from backend.core.services.jwt_service import JwtService
from infrastructure.database.repo.requests import RequestsRepo

router = APIRouter(
    prefix=config.api_prefix.v1.auth,
    tags=['Auth']
)


@router.post('/login')
async def user_login(
        user_login_data: LoginUserDTO,
        repo: Annotated[RequestsRepo, Depends(get_repo)],
        jwt_service: Annotated[JwtService, Depends(get_jwt_service)],
):
    interactor = LoginUserInteractor(
        request_repo=repo,
        jwt_service=jwt_service,
    )

    try:
        token = await interactor(user_login_data)
        return {'access_token': token, 'token_type': 'bearer'}
    except ValueError as e:
        return JSONResponse(content={'UNAUTHORIZED': str(e)}, status_code=401)


@router.post('/password/reset/')
async def reset_password(
        reset_password_data: LoginUserDTO,
        repo: Annotated[RequestsRepo, Depends(get_repo)],
        jwt_service: Annotated[JwtService, Depends(get_jwt_service)],
):
    await repo.user.change_password(
        username=reset_password_data.username,
        new_password=reset_password_data.password
    )

    interactor = LoginUserInteractor(
        request_repo=repo,
        jwt_service=jwt_service,
    )
    token = await interactor(reset_password_data)
    return {'access_token': token, 'token_type': 'bearer'}
