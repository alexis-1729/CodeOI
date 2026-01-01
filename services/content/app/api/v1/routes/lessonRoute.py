from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.services.lessonService import LessonService
from app.repositories.lessonRepository import LessonDTO
from app.schemas.lessonSchema import lessonCreate, lessonResponse
from app.db.database import get_db
from uuid import UUID

router = APIRouter()


async def get_lesson_service(db: AsyncSession = Depends(get_db))-> LessonService:
    repository = LessonDTO(db)
    serv = LessonService(repository)
    return serv

@router.post("/create", response_model=lessonResponse, status_code=status.HTTP_201_CREATED)
async def create_lesson(
    data: lessonCreate,
    service: LessonService = Depends(get_lesson_service)
) -> lessonResponse:
    """
    Crea un nuevo lesson
    """
    lesson = await service.createlesson(data)
    if not lesson:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="No se pudo crear el lesson"
        )
    return lesson

@router.get("/get/{id_level}", response_model=list[lessonResponse])
async def get_lessons_by_level(
    id_level: UUID,
    service: LessonService = Depends(get_lesson_service)
) -> list[lessonResponse]:
    """
    Obtiene todos los lessons de un nivel
    """
    lessons = await service.getLesson(id_level)
    if not lessons:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No se encontraron lessons para este nivel"
        )
    return lessons