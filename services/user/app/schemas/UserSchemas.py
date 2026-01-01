from pydantic import BaseModel, ConfigDict
from datetime import datetime
from uuid import UUID

class UserCreate(BaseModel):
    id_auth: UUID
    name: str
    lastname: str
    school: str
    grade_date: datetime

class UserResponse(BaseModel):
    model_config = ConfigDict(from_attributes = True)
    name: str
    lastname: str
    school: str
    grade_date: datetime