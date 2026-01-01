from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.db.models.ModelLevel import Level
from app.schemas.levelSchema import levelCreate, levelResponse
from uuid import UUID
import logging

class LevelDTO:
    def __init__(self, db: AsyncSession):
        self.db = db
        self.logger = logging.getLogger("LevelDTO")

    async def create_level(self, data: levelCreate)-> levelResponse | None:
        try:
            new_level = Level(**data.model_dump())
            self.db.add(new_level)
            await self.db.commit()
            await self.db.refresh(new_level)
            return levelResponse.model_validate(new_level)
        except Exception as e:
            await self.db.rollback()
            self.logger.error(f"Error en el servidor: {e}")
            return None
        
    async def get_level_by_id(self, id: UUID)-> levelResponse | None:
        try:
            level = select(Level).filter(Level.id_level == id)
            query = await self.db.execute(level)
            get = query.scalars().first()
            if not get:
                self.logger.info("No se encontro el registro")
                return None
            return levelResponse.model_validate(get)
        except Exception as e:
            self.logger.error(f"Error en el servidor: {e}")
            return None
        
    async def get_levels(self)-> list[levelResponse] | None:
        try:
            result = await self.db.execute(select(Level))
            get = result.scalars().all()
            if not get:
                self.logger.info("Algo ocurrio y no se pudo obtener el resultado")
            return get
        except Exception as e:
            self.logger.error(f"Erroe en el servidor: {e}")
            return None