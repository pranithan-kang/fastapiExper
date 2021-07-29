from fastapi import FastAPI
import uvicorn

from api.endpoints.route_exper import route_exper_router
from api.endpoints.depend_exper import depend_exper_router
from api.endpoints.logging_exper import logging_exper_router
from api.endpoints.http_exception_exper import http_exception_exper_router

from api.middleware.sample_middleware_1 import SampleMiddleware1
from api.middleware.sample_middleware_2 import SampleMiddleware2
from api.middleware.log_middleware import LogMiddleware
    

app = FastAPI()

from fastapi import Request, Response

app.add_middleware(SampleMiddleware1)
app.add_middleware(LogMiddleware)
app.add_middleware(SampleMiddleware2)

app.include_router(route_exper_router)
app.include_router(depend_exper_router)
app.include_router(logging_exper_router)
app.include_router(http_exception_exper_router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
