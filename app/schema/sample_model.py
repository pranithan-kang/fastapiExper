from typing import Union
from pydantic import BaseModel

class SampleModel(BaseModel):
    id: int
    obj: Union[int, str]
