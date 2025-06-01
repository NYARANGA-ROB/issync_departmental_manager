
from pydantic import BaseModel
from datetime import datetime
#import os


class Project(BaseModel):
    title: str
    description: str
    user_id: str
    deadline: datetime
   