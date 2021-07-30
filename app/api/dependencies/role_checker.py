from typing import List, Set
from fastapi.exceptions import HTTPException
from fastapi.param_functions import Depends

from app.api.dependencies.get_current_roles import get_current_roles

class RoleChecker:
    def __init__(self, allowed_roles: Set[str]):
        self.allowed_roles = allowed_roles

    def __call__(self, roles: Set[str] = Depends(get_current_roles)):
        ir = roles.intersection(self.allowed_roles)
        if len(ir) == 0 :
            raise HTTPException(status_code=403, detail="Operation not permitted")
        return ir

def role_checker(allowed_roles: Set[str] = None):
    async def dpd_handler(roles: Set[str] = Depends(get_current_roles)):
        ir = roles.intersection(allowed_roles)
        if len(ir) == 0 :
            raise HTTPException(status_code=403, detail="Operation not permitted")
        return ir
    return dpd_handler