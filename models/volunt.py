from sqlalchemy import Column, String, Integer, TIMESTAMP, ForeignKey
from db.database import Base
from datetime import datetime
# from sqlalchemy.orm import relationship

class Volunt(Base):
    __tablename__ = "volunteer"

    volunt_id = Column(Integer, primary_key=True, index=True)
   

    volunt_name = Column(String, nullable=False)
    phone_number = Column(String, nullable=False)
    email = Column(String)
    password = Column(String, nullable=False)
    applied_at = Column(TIMESTAMP(timezone=True), default=datetime.utcnow)
    







