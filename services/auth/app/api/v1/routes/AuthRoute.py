from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.services.AuthService import AuthService
from app.schemas.AuthSchemas import AuthCreate, AuthResponse
from app.db.database import get_db
from app.repositories.AuthRepository import AuthDTO
router = APIRouter()

async def get_service(db: AsyncSession = Depends(get_db))-> AuthService:
    dto = AuthDTO(db)
    serv = AuthService(dto)
    return serv

@router.post("/register", response_model = AuthResponse)
async def register(
    data:AuthCreate, service: AuthService = Depends(get_service)):
        user = await service.register(data)
        if not user:
            raise(
                HTTPException(status_code = 404, detail = "No se pudo registrar")
            )
        return user

@router.post("/login", response_model=AuthResponse)
async def login(
          data: AuthCreate, service: AuthService=Depends(get_service)):
            user = await service.login(data)
            if not user:
                   raise(
                          HTTPException(status_code = 404, detail="Error en el login")
                   ) 
            return user