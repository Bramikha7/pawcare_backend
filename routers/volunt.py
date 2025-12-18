from fastapi import APIRouter, Depends,HTTPException
from sqlalchemy.orm import Session
from dependencies import get_db
from models.volunt import Volunt
from schemas.volunt import VolunteerCreate,VolunteerUpdate,VolunteerLogin
from datetime import datetime




router = APIRouter(prefix="/volunteers", tags=["Volunteers"])

@router.post("/")
def create_volunteer(volunteer: VolunteerCreate, db: Session = Depends(get_db)):
    new_volunteer = Volunt(
        volunt_name=volunteer.volunt_name,
        phone_number=volunteer.phone_number,
        email=volunteer.email,
        password=volunteer.password
    )
    db.add(new_volunteer)
    db.commit()
    db.refresh(new_volunteer)
    response = {
        "volunt_id": new_volunteer.volunt_id,
        "volunt_name": new_volunteer.volunt_name,
        "phone_number": new_volunteer.phone_number,
        "email": new_volunteer.email,
        "applied_at": new_volunteer.applied_at,
        "password": new_volunteer.password
    }
    return response


@router.post("/signin")
def volunteer_signin(credentials: VolunteerLogin, db: Session = Depends(get_db)):
    volunteer = db.query(Volunt).filter(Volunt.email == credentials.email).first()

    if not volunteer:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    if credentials.password != volunteer.password:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    return {"message": "Signed in successfully", "volunt_id": volunteer.volunt_id}

@router.get("/")
def get_all_volunteers(db: Session = Depends(get_db)):
    volunteers = db.query(Volunt).all()
    result = []
    for v in volunteers:
        result.append({
            "volunt_id": v.volunt_id,
            "volunt_name": v.volunt_name,
            "phone_number": v.phone_number,
            "email": v.email,
            "applied_at": v.applied_at,
        })
    return result


@router.get("/{volunt_id}")
def get_volunteer(volunt_id: int, db: Session = Depends(get_db)):
    volunteer = db.query(Volunt).filter(Volunt.volunt_id == volunt_id).first()
    if not volunteer:
        raise HTTPException(status_code=404, detail="Volunteer not found")
    return {
        "volunt_id": volunteer.volunt_id,
        "volunt_name": volunteer.volunt_name,
        "phone_number": volunteer.phone_number,
        "email": volunteer.email,
        "applied_at": volunteer.applied_at,
    }

@router.put("/{volunt_id}")
def update_volunteer(volunt_id: int, volunteer_update: VolunteerUpdate, db: Session = Depends(get_db)):
    volunteer = db.query(Volunt).filter(Volunt.volunt_id == volunt_id).first()
    if not volunteer:
        raise HTTPException(status_code=404, detail="Volunteer not found")

    if volunteer_update.volunt_name is not None:
        volunteer.volunt_name = volunteer_update.volunt_name
    if volunteer_update.phone_number is not None:
        volunteer.phone_number = volunteer_update.phone_number
    if volunteer_update.email is not None:
        volunteer.email=volunteer_update.email    

    db.commit()
    db.refresh(volunteer)
    return volunteer

@router.delete("/{volunt_id}")
def delete_volunteer(volunt_id: int, db: Session = Depends(get_db)):
    volunteer = db.query(Volunt).filter(Volunt.volunt_id == volunt_id).first()
    if not volunteer:
        raise HTTPException(status_code=404, detail="Volunteer not found")
    
    db.delete(volunteer)
    db.commit()
    return {"message": f"Volunteer with id {volunt_id} has been deleted"}


