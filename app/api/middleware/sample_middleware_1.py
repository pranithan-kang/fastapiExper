from fastapi import Request, Response
from starlette.middleware.base import BaseHTTPMiddleware

class SampleMiddleware1(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        s = request.state
        response: Response = await call_next(request)
        response.headers["TEST-HEADER-1"] = "TEST_VALUE_1"
        return response