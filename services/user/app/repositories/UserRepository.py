from sqlalchemy.ext.asyncio import AsyncSession
from app.db.models.ModelUser import User
from sqlalchemy import select
from app.schemas.UserSchemas import UserCreate, UserResponse
from uuid import UUID
import logging

class UserDTO:
    def __init__(self, db: AsyncSession):
        self.db = db
        self.logger = logging.getLogger("UserDTO")
    
    async def create_user(self,data: UserCreate)-> UserResponse | None:
        try:
            user = User(**data.model_dump())
            self.db.add(user)
            await self.db.commit()
            await self.db.refresh(user)
            return UserResponse.model_validate(user)
        except Exception as e:
            await self.db.rollback()
            self.logger.error(f"Error en el servidor: {e}")
            return None
    
    async def get_user(self, id: UUID)-> UserResponse | None:
        try:
            user = select(User).filter(User.id_auth == id)
            result = await self.db.execute(user)
            get = result.scalars().first()
            if not get:
                self.logger.info("No se encontro el usuario")
                return None
            return UserResponse.model_validate(get)
        except Exception as e:
            self.logger.error(f"Error en el servidor: {e}")
            return None