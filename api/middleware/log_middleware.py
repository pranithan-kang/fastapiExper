from datetime import date
from fastapi import Request, Response, HTTPException
from starlette.middleware.base import BaseHTTPMiddleware

class LogMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        s = request.state
        response: Response = await call_next(request)

        log_obj = {
            "timestamp": date.today(),
            "endpoint": request.url.path,
            "activity" : None if not hasattr(request.state, "activity") else request.state.activity,
            "detail" : None if not hasattr(request.state, "detail") else request.state.detail,
            "status" : "success" if 200 <= response.status_code <= 299 else "failed"
        }

        # TODO: Logging in case of Response is OK goes here..
        print(log_obj)

        return response