from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.db.models.ModelLesson import Lesson 
from app.schemas.lessonSchema import lessonCreate, lessonResponse
from uuid import UUID
import logging

class LessonDTO:
    def __init__(self, db: AsyncSession):
        self.db = db
        self.logger = logging.getLogger("LessonDTO")

    async def create_lesson(self, data: lessonCreate)-> lessonResponse | None:
        try:
            new_lesson = Lesson(**data.model_dump())
            self.db.add(new_lesson)
            await self.db.commit()
            await self.db.refresh(new_lesson)
            return lessonResponse.model_validate(new_lesson)
        except Exception as e:
            await self.db.rollback()
            self.logger.error(f"Error en el servidor: {e}")
            return None
        
    async def get_lessons_by_topic(self, id_topic: UUID)-> list[lessonResponse] | None:
        try:
            lesson = select(Lesson).filter(Lesson.id_topic == id_topic)
            result = await self.db.execute(lesson)
            get = result.scalars().all()
            if not get:
                self.logger.info(f"No se encontraron los topics")
                return None
            return [lessonResponse.model_validate(lesson) for lesson in get]
        except Exception as e:
            self.logger.error(f"Error en el servidor: {e}")
            return None

        