from sqlalchemy import (
    Boolean,
    Column,
    ForeignKey,
    Integer,
    String,
    DateTime,
    Float,
    Text,
    JSON,
)
from sqlalchemy.orm import relationship

from db.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    email = Column(String)
    full_username = Column(String)
    role = Column(Integer)
    is_active = Column(Integer)
    last_login = Column(DateTime)
    created_date = Column(DateTime)
    login_fail = Column(Integer)
    department = Column(String)
    description = Column(String)

    # containers = relationship("Container", back_populates="owner")
