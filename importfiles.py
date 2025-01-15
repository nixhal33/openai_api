from pydantic import BaseModel
from typing import Optional

class movies(BaseModel):
    title:str
    year:int
    storyline:Optional[str]=None # this is if the value is optional or not need to give any storyline
