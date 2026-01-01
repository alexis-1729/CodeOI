from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.db.models.ModelTopic import Topic
from app.schemas.topicSchema import topicCreate, topicResponse
from uuid import UUID
import logging

class TopicDTO:
    def __init__(self, db: AsyncSession):
        self.db = db
        self.logger = logging.getLogger("TopicDTO")

    async def create_topic(self, data: topicCreate)-> topicResponse | None:
        try:
            new_topic = Topic(**data.model_dump())
            self.db.add(new_topic)
            await self.db.commit()
            await self.db.refresh(new_topic)
            return topicResponse.model_validate(new_topic)
        except Exception as e:
            await self.db.rollback()
            self.logger.error(f"Error en el servidor: {e}")
            return None
        
    async def get_topics_by_level(self, id_level: UUID)-> list[topicResponse] | None:
        try:
            topic = select(Topic).filter(Topic.level_id == id_level)
            result = await self.db.execute(topic)
            get = result.scalars().all()
            if not get:
                self.logger.info(f"No se encontraron los topics")
                return None
            return [topicResponse.model_validate(topic) for topic in get]
        except Exception as e:
            self.logger.error(f"Error en el servidor: {e}")
            return None

        