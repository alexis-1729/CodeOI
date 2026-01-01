from pydantic import BaseModel, ConfigDict
from datetime import datetime
from uuid import UUID

class topicCreate(BaseModel):
    title: str
    description: str
    created_at: datetime
    level_id: UUID

class topicResponse(BaseModel):
     model_config = ConfigDict(from_attributes = True)
     id_topic: UUID
     title: str
     description: str
     created_at: datetime
     level_id: UUID

# class levelTopicCreate(BaseModel):
#      id_level: UUID

# class levelTopicResponse(BaseModel):
#      id_topicLevel: UUID
#      id_level: UUID
