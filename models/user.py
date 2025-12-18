
from sqlalchemy import Column, Integer, String, Boolean, TIMESTAMP
from db.database import Base
# from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String)
    email = Column(String, index=True, unique=True)
    password = Column(String)
    role = Column(String)
    is_active = Column(Boolean, default=True)
    created_at = Column(TIMESTAMP(timezone=True))

    