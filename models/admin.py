

from sqlalchemy import Column, Integer, ForeignKey
# from sqlalchemy.orm import relationship
from db.database import Base

class Admin(Base):
    __tablename__ = "admins"

    admin_id = Column(Integer, primary_key=True, index=True) # Fixed 'Index' to 'index'
    



# class ContactMessage(Base):
#     __tablename__ = "contact_messages"
    
#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String)
#     email = Column(String)
#     message = Column(Text)
#     status = Column(String, default="unread")
#     created_at = Column(DateTime, default=datetime.utcnow)