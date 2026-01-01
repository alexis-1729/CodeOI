from pydantic import BaseModel, ConfigDict
from uuid import UUID

class AuthCreate(BaseModel):
    email: str
    password_hash: str

class AuthResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    id_auth: UUID
    role: str