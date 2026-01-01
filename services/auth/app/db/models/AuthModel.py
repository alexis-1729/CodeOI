from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID
from app.db.database import Base
import uuid

class Auth(Base):
    __tablename__ ="auth"
    id_auth = Column(UUID(as_uuid = True), primary_key = True,default = uuid.uuid4)
    email = Column(String(50), nullable = False)
    password_hash = Column(String, nullable = False)
    role = Column(String(10), default = "user")