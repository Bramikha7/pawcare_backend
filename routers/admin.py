# from fastapi import APIRouter, Depends, HTTPException, status
# from sqlalchemy.orm import Session
# from sqlalchemy import desc
# from datetime import datetime
# from typing import List, Optional
# from pydantic import BaseModel
# from dependencies import get_db
# from models.admin import Donation, CaseReport,VaccinationDrive,ContactMessage

# # Assuming you have these imports from your existing setup
# # from .database import get_db
# # from .models import User, Donation, CaseReport, VaccinationDrive, ContactMessage

# router = APIRouter(prefix="/admin", tags=["admin"])

# # Pydantic Schemas
# class DonationResponse(BaseModel):
#     name: str
#     amount: float
#     date: datetime

#     class Config:
#         from_attributes = True

# class VolunteerResponse(BaseModel):
#     name: str
#     city: str
#     role: str

#     class Config:
#         from_attributes = True

# class CaseReportResponse(BaseModel):
#     location: str
#     dogs: int
#     status: str

#     class Config:
#         from_attributes = True

# class VaccinationDriveResponse(BaseModel):
#     id: int
#     title: str
#     location: str
#     date: datetime
#     time: str
#     status: str

#     class Config:
#         from_attributes = True

# class VaccinationDriveCreate(BaseModel):
#     title: str
#     location: str
#     date: datetime
#     time: str
#     status: str = "scheduled"

# class ContactMessageResponse(BaseModel):
#     name: str
#     email: str
#     message: str
#     status: str

#     class Config:
#         from_attributes = True

# # Endpoints
# @router.get("/donations", response_model=List[DonationResponse])
# def get_recent_donations(
#     limit: int = 10,
#     db: Session = Depends(get_db)
# ):
#     donations = db.query(Donation)\
#         .order_by(desc(Donation.date))\
#         .limit(limit)\
#         .all()
#     return donations

# # @router.get("/volunteers", response_model=List[VolunteerResponse])
# # def get_new_volunteers(
# #     limit: int = 10,
# #     db: Session = Depends(get_db)
# # ):
# #     volunteers = db.query(User)\
# #         .filter(User.role == "volunteer")\
# #         .order_by(desc(User.created_at))\
# #         .limit(limit)\
# #         .all()
# #     return [{
# #         "name": v.name,
# #         "city": v.city,
# #         "role": v.role
# #     } for v in volunteers]

# @router.get("/case-reports", response_model=List[CaseReportResponse])
# def get_case_reports(
#     limit: int = 10,
#     db: Session = Depends(get_db)
# ):
#     reports = db.query(CaseReport)\
#         .order_by(desc(CaseReport.created_at))\
#         .limit(limit)\
#         .all()
#     return reports

# @router.get("/vaccination-drives", response_model=List[VaccinationDriveResponse])
# def get_vaccination_drives(
#     db: Session = Depends(get_db)
# ):
#     drives = db.query(VaccinationDrive)\
#         .order_by(VaccinationDrive.date)\
#         .all()
#     return drives

# @router.post("/vaccination-drives", response_model=VaccinationDriveResponse, status_code=status.HTTP_201_CREATED)
# def create_vaccination_drive(
#     drive: VaccinationDriveCreate,
#     db: Session = Depends(get_db)
# ):
#     new_drive = VaccinationDrive(
#         title=drive.title,
#         location=drive.location,
#         date=drive.date,
#         time=drive.time,
#         status=drive.status
#     )
#     db.add(new_drive)
#     db.commit()
#     db.refresh(new_drive)
#     return new_drive

# @router.get("/contact-messages", response_model=List[ContactMessageResponse])
# def get_contact_messages(
#     limit: int = 20,
#     db: Session = Depends(get_db)
# ):
#     messages = db.query(ContactMessage)\
#         .order_by(desc(ContactMessage.created_at))\
#         .limit(limit)\
#         .all()
#     return messages