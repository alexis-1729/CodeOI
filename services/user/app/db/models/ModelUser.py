from sqlalchemy import String, Column, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from app.db.database import Base
import uuid

class User(Base):
    __tablename__ ="user"
    id_user = Column(UUID(as_uuid = True), primary_key = True, default = uuid.uuid4)
    id_auth = Column(UUID(as_uuid =True), nullable = True)
    name = Column(String(30), nullable = True)
    lastname = Column(String(50), nullable = True)
    school = Column(String(50), nullable = True)
    grade_date = Column(DateTime(timezone = True), server_default = func.now())