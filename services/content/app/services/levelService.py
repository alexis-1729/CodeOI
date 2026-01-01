from app.repositories.levelRepository import LevelDTO
from app.schemas.levelSchema import levelCreate, levelResponse
from uuid import UUID

class LevelService:
    def __init__(self, repsoitory: LevelDTO):
        self.repository = repsoitory

    async def createLevel(self, data: levelCreate)-> levelResponse | None:
        level = await self.repository.create_level(data)
        if level:
            return level
        return None
    
    async def getLevel(self, id_level: UUID)-> levelResponse | None:
        level = await self.repository.get_level_by_id(id_level)
        if level:
            return level
        return None
    
    async def get_all_levels(self)-> list[levelResponse] | None:
        levels = await self.repository.get_levels()
        if levels:
            return levels
        return None