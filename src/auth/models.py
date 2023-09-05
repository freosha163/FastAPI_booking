from datetime import datetime
import uuid
from sqlalchemy import (Integer,
                        String,
                        TIMESTAMP,
                        ForeignKey,
                        Table,
                        Column,
                        JSON,
                        UUID,
                        Boolean,
                        )
from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTableUUID
from database import Base, metadata


class Role(Base):
    __tablename__ = 'role'
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    permissions = Column(JSON)


class User(SQLAlchemyBaseUserTableUUID, Base):
    __tablename__ = 'user'
    __table_args__ = {'extend_existing': True}
    id = Column(UUID, primary_key=True, default=uuid.uuid4)
    username = Column(String, nullable=False)
    email = Column(String, nullable=False)
    username = Column(String, nullable=False)
    registered_at = Column(TIMESTAMP, default=datetime.utcnow)
    role_id = Column(Integer, ForeignKey(Role.id))
    hashed_password: str = Column(String(length=1024), nullable=False)
    is_active: bool = Column(Boolean, default=True, nullable=False)
    is_superuser: bool = Column(Boolean, default=False, nullable=False)
    is_verified: bool = Column(Boolean, default=False, nullable=False)
