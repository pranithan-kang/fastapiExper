from fastapi.routing import APIRouter
from sqlalchemy.orm.session import Session
from starlette.requests import Request
from fastapi.param_functions import Depends, Query

import app.api.dependencies.db as dbm
from app.repository import sample_a

orm_exper_router = APIRouter(prefix="/orm-exper")

@orm_exper_router.get("/get")
async def get(
    db_session: Session = Depends(dbm.get_db)
):
    return sample_a.get_records_table_a(db_session)

@orm_exper_router.get("/add")
async def add(
    db_session: Session = Depends(dbm.get_db)
):
    sample_a.add_records_table_a(db_session)