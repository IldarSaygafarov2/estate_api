import uvicorn
from fastapi import FastAPI

from backend.api import router as api_router

from backend.app.config import config
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
main_app = FastAPI()

main_app.mount("/media", StaticFiles(directory="media"), name="media")

main_app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)


main_app.include_router(api_router)

if __name__ == '__main__':
    uvicorn.run(
        'app:main_app',
        host=config.run_api.api_host,
        port=config.run_api.api_port,
        reload=True
    )