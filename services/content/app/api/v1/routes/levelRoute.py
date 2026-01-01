from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.services.levelService import LevelService
from app.repositories.levelRepository import LevelDTO
from app.schemas.levelSchema import levelCreate, levelResponse
from app.db.database import get_db
from uuid import UUID

router = APIRouter()

async def get_level_service(db: AsyncSession = Depends(get_db))-> LevelService:
    repository = LevelDTO(db)
    return LevelService(repository)

@router.post("/create", response_model = levelResponse)
async def create_level(
    data: levelCreate,
    service: LevelService = Depends(get_level_service)
)-> levelResponse:
    """
    Crea un nuevo nivel
    """
    level = await service.createLevel(data)
    if not level:
        raise HTTPException(
            status_code = status.HTTP_400_BAD_REQUEST,
            detail = "No se pudo crear un nuevo registro"
            )
    return level

@router.get("/get", response_model = list[levelResponse])
async def get_levels(
    service: LevelService = Depends(get_level_service)
):
    """
    Obtiene los niveles
    """
    level = await service.get_all_levels()
    if not level:
        raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="No se encontraron topics para este nivel"
            )
    return level


