from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.db.models.AuthModel import Auth
from app.schemas.AuthSchemas import AuthCreate, AuthResponse
from app.services.TokenService import verify_password, get_password_hash
from uuid import UUID
import logging

class AuthDTO:

    def __init__(self, db: AsyncSession):
        self.db = db
        self.logger = logging.getLogger("AuthDTO")

    async def create_auth(self, data: AuthCreate)-> AuthResponse | None:
        try:
            user = select(Auth).filter(Auth.email == data.email)
            query = await self.db.execute(user)
            get = query.scalars().first()
            if get:
                self.logger.info("El usuario ya existe")
                return None
            
            hashed = get_password_hash(data.password_hash)
            new_auth = Auth(email=data.email, password_hash=hashed)
            
            self.db.add(new_auth)
            await self.db.commit()
            await self.db.refresh(new_auth)
            return AuthResponse.model_validate(new_auth)
        except Exception as e:
            await self.db.rollback()
            self.logger.error(f"Error en el servidor. {e}")
            return None
        
    async def get_login(self, data: AuthCreate)-> AuthResponse | None:
        try:
            user = select(Auth).filter(Auth.email == data.email)
            query = await self.db.execute(user)
            get = query.scalars().first()
            if not get:
                self.logger.info("No se encontro el user")
                return None
            if not verify_password(data.password_hash, get.password_hash):
                self.logger.info("Las contraseñas no coinciden")
                return None
            return AuthResponse.model_validate(get)
        except Exception as e:
            self.logger.error("Error en el servidor: {e}")
            return None
        