import datetime

from pydantic import BaseModel
from sqlalchemy import String, Enum
from sqlalchemy.orm import Mapped, mapped_column


class Dep(BaseModel):
    db_name:str
    username:str

