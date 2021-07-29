from typing import List, Optional
from schema.sample_tuple import SampleTuple
from schema.sample_model import SampleModel
from fastapi import APIRouter, UploadFile, Depends, Security, Body, File, HTTPException, Request
from fastapi.params import Body
from pydantic import BaseModel
import pandas as pd
import helper.jwt_helper as jwt_helper

depend_exper_router = APIRouter()

def role_spec(roles: List[str] = None):
    async def dpd_handler(role: Optional[str], request: Request):
        # TODO: Authentication

        # in case of all-role
        if roles is None: return request.headers

        if role not in roles: raise HTTPException(403)

        # TODO: Return CurrentUser object
        return request.headers
    return dpd_handler

@depend_exper_router.get("/test-depend-1")
async def read_depend_1(
    extrac = Depends(role_spec(["Role_1"]))
):
    return extrac


@depend_exper_router.get("/test-depend-2")
async def read_depend_2(
    extrac = Depends(role_spec(["Role_1", "Role_2"]))
):
    return extrac


@depend_exper_router.get("/test-depend-3")
async def read_depend_3(
    extrac = Depends(role_spec())
):
    return extrac