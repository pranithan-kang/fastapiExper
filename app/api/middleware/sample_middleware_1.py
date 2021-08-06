from fastapi import Request, Response
from starlette.middleware.base import BaseHTTPMiddleware

from app.api.dependencies.db import get_db

class SampleMiddleware1(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        s = request.state

        db = [d for d in get_db()][0]

        response: Response = await call_next(request)
        response.headers["TEST-HEADER-1"] = "TEST_VALUE_1"
        return response