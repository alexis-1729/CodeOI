from pydantic import BaseModel, ConfigDict
from uuid import UUID

class levelCreate(BaseModel):
    name: str
    description: str
    img_url: str
    
class levelResponse(BaseModel):
    model_config= ConfigDict(from_attributes = True)
    id_level: UUID
    name: str
    description: str
    img_url: str