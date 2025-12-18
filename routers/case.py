from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models.volunt import Volunt
from models.case import CaseReport
from schemas.case import (CaseReportCreate,CaseReportUpdate,CaseReportResponse)
from dependencies import get_db


router = APIRouter(prefix="/case-reports",tags=["Case Reports"])

@router.get("/", response_model=list[CaseReportResponse])
def get_all_case_reports(db: Session = Depends(get_db)):
    reports = db.query(CaseReport).all()
    return reports

@router.get("/{case_id}", response_model=CaseReportResponse)
def get_case_report(case_id: int, db: Session = Depends(get_db)):
    report = db.query(CaseReport).filter(CaseReport.case_id == case_id).first()

    if not report:
        raise HTTPException(status_code=404, detail="Case report not found")

    return report

@router.post("/", response_model=CaseReportResponse)
def create_case_report(case: CaseReportCreate,db: Session = Depends(get_db)):
    
    new_case = CaseReport(
        volunt_id=case.volunt_id,
        name=case.name,
        phone=case.phone,
        email=case.email,
        address=case.address,
        city=case.city,
        pincode=case.pincode,
        number_of_dogs=case.number_of_dogs,
        urgency_level=case.urgency_level,
        description=case.description,
        best_time_to_visit=case.best_time_to_visit
    )

    db.add(new_case)
    db.commit()
    db.refresh(new_case)

    case_new={
        "case_id": new_case.case_id,
        "volunt_id": new_case.volunt_id,
        "name": new_case.name,
        "phone": new_case.phone,
        "email": new_case.email,
        "address": new_case.address,
        "city": new_case.city,
        "pincode": new_case.pincode,
        "number_of_dogs": new_case.number_of_dogs,
        "urgency_level": new_case.urgency_level,
        "description": new_case.description,
        "best_time_to_visit": new_case.best_time_to_visit
    }
    return case_new
@router.put("/{case_id}", response_model=CaseReportResponse)
def update_case_report(case_id: int,case_update: CaseReportUpdate,db: Session = Depends(get_db)):
    report = db.query(CaseReport).filter(CaseReport.case_id == case_id).first()

    if not report:
        raise HTTPException(status_code=404, detail="Case report not found")
    
    update_data = case_update.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(report, key, value)

    db.commit()
    db.refresh(report)

    return report



