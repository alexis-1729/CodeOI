from app.repositories.topicRepository import TopicDTO
from app.schemas.topicSchema import topicCreate, topicResponse
from uuid import UUID

class TopicService:
    def __init__(self, repository: TopicDTO):
        self.repository = repository

    async def createTopic(self, data: topicCreate)-> topicResponse | None:
        topic = await self.repository.create_topic(data)
        if topic: 
            return topic
        return None
    
    async def getTopics(self, id_level: UUID):
        topics = await self.repository.get_topics_by_level(id_level)
        if topics:
            return topics
        return None