from fastapi import FastAPI
from sqlalchemy.engine import create_engine
import uvicorn
from app import config

from app.api.endpoints.route_exper import route_exper_router
from app.api.endpoints.depend_exper import depend_exper_router
from app.api.endpoints.logging_exper import logging_exper_router
from app.api.endpoints.http_exception_exper import http_exception_exper_router
from app.api.endpoints.orm_exper import orm_exper_router
from app.api.middleware.sample_middleware_1 import SampleMiddleware1
from app.api.middleware.sample_middleware_2 import SampleMiddleware2
from app.api.middleware.log_middleware import LogMiddleware
import app.api.dependencies.db as dbm

app = FastAPI()

from fastapi import Request, Response

app.add_middleware(SampleMiddleware1)
app.add_middleware(LogMiddleware)
app.add_middleware(SampleMiddleware2)

app.include_router(route_exper_router)
app.include_router(depend_exper_router)
app.include_router(logging_exper_router)
app.include_router(http_exception_exper_router)
app.include_router(orm_exper_router)

@app.on_event("startup")
def app_startup():
    dbm.engine = create_engine(config.CONNECTION_STRING)

@app.on_event("shutdown")
def app_shutdown():
    if dbm.engine:
        dbm.engine.close()

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
