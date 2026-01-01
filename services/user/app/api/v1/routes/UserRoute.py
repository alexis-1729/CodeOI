from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.database import get_db
from app.schemas.UserSchemas import UserCreate, UserResponse
from app.services.UserService import UserService
from app.repositories.UserRepository import UserDTO
from uuid import UUID

async def get_user_service(db: AsyncSession = Depends(get_db))-> UserService:
    dto = UserDTO(db)
    serv = UserService(dto)
    return serv

router = APIRouter()
@router.post("/create", response_model = UserResponse)
async def create_user(data: UserCreate, 
                      service: UserService = Depends(get_user_service))-> UserResponse | None:
    user = await service.createUser(data)
    if not user:
        raise HTTPException(
            status_code = 404,
            detail = "No se pudo crear el usuario"
        )
    return user

@router.post("/get")
async def get_user(id: UUID,
                   service: UserService = Depends(get_user_service))-> UserResponse | None:
    user = await service.getUser(id)
    if not user:
        raise HTTPException(
            status_code = 404,
            detail = "No se encontro un usuario"
        )
    return user
