from typing import List, Optional
from schema.sample_tuple import SampleTuple
from schema.sample_model import SampleModel
from fastapi import APIRouter, UploadFile, Depends, Security, Body, File, HTTPException, Request
from fastapi.params import Body
from pydantic import BaseModel
import pandas as pd
import helper.jwt_helper as jwt_helper

logging_exper_router = APIRouter()

@logging_exper_router.get("/test-log-1")
async def read_test_log_1(
    request: Request
):
    request.state.activity = "Create"

    request.state.detail = "test log 1"
    return { "message": "test-log-1" }

@logging_exper_router.get("/test-log-2")
async def read_test_log_2(
    request: Request
):
    request.state.activity = "Read"

    request.state.detail = "test log 2"
    return { "message": "test-log-2" }

@logging_exper_router.get("/test-log-exception")
async def read_test_log_exception(
    request: Request
):
    request.state.activity = "Update"
    
    request.state.detail = "test log exception"
    raise HTTPException(403, {
        "httpStatus": 403,
        "message": "Permission Denied"
    })
    return { "message": "test-log-2" }
