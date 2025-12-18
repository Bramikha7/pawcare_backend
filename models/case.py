from sqlalchemy import Column, Integer, String, Text, DateTime,ForeignKey,TIMESTAMP
from sqlalchemy.sql import func
# from sqlalchemy.orm import relationship
from db.database import Base

class CaseReport(Base):
    __tablename__ = "case_reports"

    case_id = Column(Integer, primary_key=True, index=True)
    volunt_id = Column(Integer, ForeignKey("volunteer.volunt_id"),index=True)
    name = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    email = Column(String, nullable=False)
    address = Column(Text, nullable=False)
    city = Column(String, nullable=False)
    pincode = Column(String, nullable=False)
    number_of_dogs = Column(Integer, nullable=False)
    urgency_level = Column(String, nullable=False)
    description = Column(Text)
    best_time_to_visit = Column(String)
    status = Column(String, default="Submitted")
    reported_at = Column(DateTime(timezone=True), server_default=func.now())
   
   





