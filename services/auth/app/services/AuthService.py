from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.AuthSchemas import AuthCreate, AuthResponse
from app.repositories.AuthRepository import AuthDTO

class AuthService:
    def __init__(self, dto: AuthDTO):
        self.dto = dto

    async def login(self, data: AuthCreate)-> AuthResponse | None:
        user = await self.dto.get_login(data)
        return user
    
    async def register(self, data:AuthCreate)-> AuthResponse | None:
        user = await self.dto.create_auth(data)
        return user
