from app.repositories.UserRepository import UserDTO
from app.schemas.UserSchemas import UserCreate, UserResponse
from uuid import UUID

class UserService:
    def __init__(self, dto: UserDTO):
        self.dto = dto
    
    async def createUser(self, data: UserCreate)-> UserResponse | None:
        user = await self.dto.create_user(data)
        return user
    
    async def getUser(self, id: UUID)-> UserResponse | None:
        user = await self.dto.get_user(id)
        return user