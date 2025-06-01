from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class SessionCreate(BaseModel):
    title: str
    description: Optional[str] = None
    instructor_id: str
    start_time: datetime
    duration: int  # Duration in minutes
    is_live: Optional[bool] = False

class SessionUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    start_time: Optional[datetime] = None
    duration: Optional[int] = None
    is_live: Optional[bool] = None
