from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models.volunt import Volunt
from dependencies import get_db
from models.donation import Donation
from schemas.donation import DonationResponse,DonationCreate

router = APIRouter(
    prefix="/donations",
    tags=["Donations"]
)

@router.get("/", response_model=list[DonationResponse])
def get_all_donations(db: Session = Depends(get_db)):
    donations = db.query(Donation).all()
    return donations

@router.get("/{donation_id}", response_model=DonationResponse)
def get_donation_by_id(
    donation_id: int,
    db: Session = Depends(get_db)
):
    donation = db.query(Donation).filter(Donation.id == donation_id).first()

    if donation is None:
        raise HTTPException(status_code=404, detail="Donation not found")

    return donation


@router.post("/", response_model=DonationResponse)
def create_donation(
    donation: DonationCreate,
    db: Session = Depends(get_db)
):
    volunteer=db.query(Volunt).filter(Volunt.volunt_id == donation.volunt_id).first()
    if not volunteer:
        raise HTTPException(status_code=404, detail="Volunteer not found")

    new_donation = Donation(
        volunt_id=donation.volunt_id,
        amount=donation.amount,
        payment_method=donation.payment_method,
        donor_name=donation.donor_name,
        donor_email=donation.donor_email
    )

    db.add(new_donation)
    db.commit()
    db.refresh(new_donation)

    donation_new={
        "id": new_donation.id,
        "volunt_id": new_donation.volunt_id,
        "amount": new_donation.amount,
        "payment_method": new_donation.payment_method,
        "donor_name": new_donation.donor_name,
        "donor_email": new_donation.donor_email
    }
    return donation_new