from sqlalchemy import Column, String, ForeignKey, Text, Integer
from sqlalchemy.dialects.postgresql import UUID
from app.db.database import Base
import uuid


class Lesson(Base):
    __tablename__ = "lesson"
    id_lesson = Column(UUID(as_uuid =True), primary_key = True, default = uuid.uuid4)
    title = Column(String, nullable = False)
    description = Column(String, nullable = False)
    content_md = Column(Text, nullable = True)
    code_md = Column(Text, nullable = True)
    adtional_url = Column(Text, nullable = True)
    time = Column(Integer, nullable = False)
    tags_id = Column(UUID(as_uuid = True), ForeignKey("tags.id_tag", ondelete = "CASCADE"), nullable = False)
    id_topic = Column(UUID(as_uuid =True), ForeignKey("topic.id_topic", ondelete = "CASCADE"), nullable = False)

class Tags(Base):
    __tablename__="tags"
    id_tag = Column(UUID(as_uuid =True), primary_key = True, default = uuid.uuid4)
    name = Column(String, nullable = False)


