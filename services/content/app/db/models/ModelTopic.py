from sqlalchemy import Column, String, ForeignKey, DateTime
from app.db.database import Base
from sqlalchemy.sql import func
from sqlalchemy.dialects.postgresql import UUID
import uuid

class Topic(Base):
    __tablename__ = "topic"
    id_topic = Column(UUID(as_uuid = True), primary_key = True, default = uuid.uuid4)
    title = Column(String, nullable = False)
    description = Column(String, nullable = False)
    created_at = Column(DateTime(timezone = True), server_default = func.now())
    level_id = Column(UUID(as_uuid = True), ForeignKey("level.id_level", ondelete = "CASCADE"), nullable = False)

