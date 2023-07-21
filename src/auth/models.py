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


# role = Table(
#     'role',
#     metadata,
#     Column('id', Integer, primary_key=True),
#     Column('name', String, nullable=False),
#     Column('permissions', JSON),
# )

class Role(Base):
    __tablename__ = 'role'
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    permissions = Column(JSON)

# user = Table(
#     'user',
#     metadata,
#     Column('id', UUID, primary_key=True),
#     Column('email', String, nullable=False),
#     Column('username', String, nullable=False),
#     Column('first_name', String),
#     Column('last_name', String),
#     Column('phone', String),
#     Column('hashed_password', String, nullable=False),
#     Column('registered_at', TIMESTAMP, default=datetime.utcnow),
#     Column('role_id', Integer, ForeignKey(role.c.id)),
#     Column('is_active', Boolean, default=True, nullable=False),
#     Column('is_superuser', Boolean, default=True, nullable=False),
#     Column('is_verified', Boolean, default=True, nullable=False),
# )


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
