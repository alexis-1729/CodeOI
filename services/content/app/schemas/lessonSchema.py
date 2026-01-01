from pydantic import BaseModel, ConfigDict
from uuid import UUID

class lessonCreate(BaseModel):
    title: str
    description: str
    content_md: str
    code_md: str
    aditional_md: str
    time: int
    tags_id: UUID
    id_topic: UUID

class lessonResponse(BaseModel):
     model_config = ConfigDict(from_attributes = True)
     id_lesson: UUID
     title: str
     description: str
     content_md: str
     code_md: str
     aditional_md: str
     time: int
     tags_id: UUID
     id_topic: UUID

class tagsCreate(BaseModel):
     name: str
    
class tagsResponse(BaseModel):
     id_tag: UUID
     name: str

# class topicLessonCreate(BaseModel):
#      id_topic: UUID

# class topicLessonResponse(BaseModel):
#      id_topicLesson: UUID
#      id_topic: UUID