import logging
from fastapi import FastAPI
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from datetime import datetime

# Настройка логирования
log_filename = f"logs/api_requests_{datetime.now().strftime('%Y-%m-%d')}.log"
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(log_filename),
        logging.StreamHandler()  # Дополнительно, для вывода в консоль
    ]
)
logger = logging.getLogger("api-logger")

# Создаем FastAPI приложение


# Middleware для логирования всех запросов
class RequestLoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        # Логируем информацию о запросе
        logger.info(f"Incoming request: {request.method} {request.url}")
        response = await call_next(request)
        # Логируем информацию о ответе
        logger.info(f"Response status: {response.status_code}")
        return response


