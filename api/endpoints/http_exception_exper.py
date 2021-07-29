from typing import List, Optional
from schema.sample_tuple import SampleTuple
from schema.sample_model import SampleModel
from fastapi import APIRouter, UploadFile, Depends, Security, Body, File, HTTPException, Request
from fastapi.params import Body
from pydantic import BaseModel
import pandas as pd
import helper.jwt_helper as jwt_helper

http_exception_exper_router = APIRouter()


@http_exception_exper_router.get("/test-http-exception")
async def read_test_log_1(
    request: Request
):
    raise HTTPException(456, detail={"message": "test-log-1"})
