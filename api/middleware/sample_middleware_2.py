from fastapi import Request, Response
from starlette.middleware.base import BaseHTTPMiddleware

class SampleMiddleware2(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        s = request.state
        response: Response = await call_next(request)
        response.headers["TEST-HEADER-2"] = "TEST_VALUE_2"
        return response