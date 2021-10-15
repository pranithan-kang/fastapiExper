from fastapi import Query, Request
from fastapi import APIRouter, UploadFile, Depends, Security, Body, File
from fastapi.params import Body
from pydantic import BaseModel
import pandas as pd

from enum import Enum

from app.schema.sample_tuple import SampleTuple
from app.schema.sample_model import SampleModel

import app.helper.jwt_helper as jwt_helper

route_exper_router = APIRouter()

@route_exper_router.get("/")
async def read_root():
    return {"Hello": "World"}


@route_exper_router.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}


@route_exper_router.get("/test-route")
async def test_route():
    pass


@route_exper_router.get("/test-token")
async def test_token(
    current_user=Security(jwt_helper.get_current_user,
                          scopes=["role_1", "role_2"])
):
    return {"test": "pass"}


# https://stackoverflow.com/questions/61952845/fastapi-single-parameter-body-cause-pydantic-validation-error
    """
    ###
    POST http://localhost:8000/test-single-int/

    {
    "t": 10
    }

    ###
    POST http://localhost:8000/test-single-str/

    {
    "s": "test"
    }

    ###
    POST http://localhost:8000/test-multi-int/

    {
    "s": 10,
    "t": 10
    }

    ###
    POST http://localhost:8000/test-multi-str/

    {
    "s": "test_1",
    "t": "test_2"
    }

    ###
    POST http://localhost:8000/test-multi-mix/

    {
    "s": "test",
    "t": 10
    }
    """


@route_exper_router.post("/test-single-int")
async def test_single_int(
    t: int = Body(...)
):
    pass


@route_exper_router.post("/test-single-str")
async def test_single_str(
    s: str = Body(...)
):
    pass


@route_exper_router.post("/test-multi-int")
async def test_multi_int(
    s: int = Body(...),
    t: int = Body(...),
):
    pass


@route_exper_router.post("/test-multi-str")
async def test_multi_param(
    s: str = Body(...),
    t: str = Body(...),
):
    pass


@route_exper_router.post("/test-multi-mix")
async def test_multi_param(
    s: str = Body(...),
    t: int = Body(...),
):
    pass


@route_exper_router.post("/test-model")
def test_model(
    model: SampleModel
):
    pass


@route_exper_router.post("/test-file-upload")
async def test_file_upload(
    uploadFile: UploadFile = File(...)
):
    tbl = [
        SampleTuple(col_a="value 1", col_b="value 2", col_c="value 3"),
        SampleTuple(col_a="value 4", col_b="value 5", col_c="value 6"),
        SampleTuple(col_a="value 7", col_b="value 8", col_c="value 9")]
    internal_df = pd.DataFrame.from_dict([vars(r) for r in tbl])

    f = await uploadFile.read()
    external_df = pd.read_excel(f)
    pass

@route_exper_router.get("/test-custom-named-param")
async def test_custom_named_param(
    request: Request,
    test_name: str = Query(..., alias="test.name")
):
    return test_name


class TestEnum(Enum):
    CONST_1 = "CONST_1"
    CONST_2 = "CONST_2"
    CONST_3 = "CONST_3"


@route_exper_router.post("/test-enum-param")
async def test_enum_param(
    body_param: TestEnum
):
    pass