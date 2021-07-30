from typing import List, Optional
from fastapi import APIRouter, UploadFile, Depends, Security, Body, File, HTTPException, Request
from fastapi.params import Body
from pydantic import BaseModel
import pandas as pd

from app.schema.sample_tuple import SampleTuple
from app.schema.sample_model import SampleModel

import app.helper.jwt_helper as jwt_helper
from app.api.dependencies.role_checker import RoleChecker, role_checker

depend_exper_router = APIRouter()

@depend_exper_router.get("/test-depend-1")
async def read_depend_1(
    extrac = Depends(RoleChecker(["Role_1"]))
):
    return extrac


@depend_exper_router.get("/test-depend-2")
async def read_depend_2(
    extrac = Depends(role_checker(["Role_1", "Role_2"]))
):
    return extrac


@depend_exper_router.get("/test-depend-3")
async def read_depend_3(
    extrac = Depends(role_checker())
):
    return extrac

