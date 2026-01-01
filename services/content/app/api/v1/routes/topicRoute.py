from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.services.topicService import TopicService
from app.repositories.topicRepository import TopicDTO
from app.schemas.topicSchema import topicCreate, topicResponse
from app.db.database import get_db
from uuid import UUID
router = APIRouter()

# Inyectar dependencias
async def get_topic_service(db: AsyncSession = Depends(get_db)) -> TopicService:
    repository = TopicDTO(db)
    return TopicService(repository)

@router.post("/create", response_model=topicResponse, status_code=status.HTTP_201_CREATED)
async def create_topic(
    data: topicCreate,
    service: TopicService = Depends(get_topic_service)
) -> topicResponse:
    """
    Crea un nuevo topic
    """
    topic = await service.createTopic(data)
    if not topic:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="No se pudo crear el topic"
        )
    return topic

@router.get("/get/{id_level}", response_model=list[topicResponse])
async def get_topics_by_level(
    id_level: UUID,
    service: TopicService = Depends(get_topic_service)
) -> list[topicResponse]:
    """
    Obtiene todos los topics de un nivel
    """
    topics = await service.getTopics(id_level)
    if not topics:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No se encontraron topics para este nivel"
        )
    return topics