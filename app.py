from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import ORJSONResponse
from fastapi.staticfiles import StaticFiles

from backend.api import router as api_router
from backend.app.config import config
from infrastructure.database.setup import create_engine, create_session_pool
from scripts.mock_data.create_user import add_user
from middlewares.logging import RequestLoggingMiddleware


@asynccontextmanager
async def app_lifespan(app: FastAPI):
    engine = create_engine(db=config.db)
    session_pool = create_session_pool(engine)
    async with session_pool() as session:
        await add_user(session=session)
    yield


main_app = FastAPI(lifespan=app_lifespan,
                   default_response_class=ORJSONResponse, )

main_app.mount("/media", StaticFiles(directory="media"), name="media")

origins = [
    'https://realty-360.vercel.app/real-estate',
    'http://localhost:3000',
    'https://realty-360.uz'
]

main_app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

main_app.add_middleware(RequestLoggingMiddleware)

main_app.include_router(api_router)

if __name__ == '__main__':
    uvicorn.run(
        'app:main_app',
        host=config.run_api.api_host,
        port=config.run_api.api_port,
        reload=True
    )
