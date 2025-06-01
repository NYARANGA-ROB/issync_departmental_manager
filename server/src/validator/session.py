
from pydantic import BaseModel
from datetime import datetime
#import os


class Session(BaseModel):
    title: str
    description: str
    user_id: str
    deadline: datetime
    meeting_link: str
    instructor: str
    unit_name: str
   