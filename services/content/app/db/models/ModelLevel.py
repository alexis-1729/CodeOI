from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from app.db.database import Base
import uuid

class Level (Base):
    __tablename__ = "level"
    id_level = Column(UUID(as_uuid = True), primary_key = True, default = uuid.uuid4)
    name = Column(String, nullable = False)
    description = Column(String, nullable = False)
    img_url = Column(String, nullable = False)
    

