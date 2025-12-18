from sqlalchemy import Column, Integer, String, Numeric, DateTime,ForeignKey
from db.database import Base
from datetime import datetime
# from sqlalchemy.orm import relationship

class Donation(Base):
    __tablename__ = "donations"

    id = Column(Integer, primary_key=True)
    volunt_id = Column(Integer, ForeignKey("volunteer.volunt_id"),nullable=False )
    amount = Column(Numeric(10, 2), nullable=False)
    payment_method = Column(String(50), nullable=False)
    donor_name = Column(String(100))
    donor_email = Column(String(100))
    donated_at = Column(DateTime, default=datetime.utcnow)