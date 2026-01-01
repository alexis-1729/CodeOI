from app.repositories.lessonRepository import LessonDTO
from app.schemas.lessonSchema import lessonCreate, lessonResponse
from uuid import UUID


class LessonService:

    def __init__(self, repository: LessonDTO):
        self.repository = repository
        
    async def createLesson(self, data: lessonCreate)-> lessonResponse | None:
        lesson = await self.repository.create_lesson(data)
        return lesson
    
    async def getLesson(self, id_topic: UUID):
        return await self.repository.get_lessons_by_topic(id_topic)
    
        
    
        