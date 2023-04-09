from fastapi import APIRouter, Depends, HTTPException, Response
from domain.schemas import OfficeCreate, OfficeUpdate
from domain.database import get_db
from sqlalchemy.orm import Session
from repo import office_repo

router  = APIRouter()

@router.get("/read")
def get_all_offices(db: Session = Depends(get_db)):
    offices = office_repo.get_all_offices(db)
    if offices is None:
        raise HTTPException(status_code=404, detail="Office not found")
    return offices

@router.get("/read/{office_id}")
def get_office(office_id: int, db: Session = Depends(get_db)):
    office = office_repo.get_office(db, office_id)
    if office is None:
        raise HTTPException(status_code=404, detail="Office not found")
    return office 

@router.post("/create")
def create_office(office: OfficeCreate, db: Session = Depends(get_db)):
    created_office = office_repo.create_office(db, office)
    response = Response(status_code=201)
    response.headers["Location"] = f"/offices/read/{created_office.id}"
    return response


@router.put("/update/{office_id}")
def update_office(office_id: int, office: OfficeUpdate, db: Session = Depends(get_db)):
    updated_office = office_repo.update_office(db, office_id, office)
    if updated_office is None:
        raise HTTPException(status_code=404, detail="Office not found")
    return {"message": "Office updated successfully"}


@router.delete("/delete/{office_id}")
def delete_office(office_id: int, db: Session = Depends(get_db)):
    deleted_office = office_repo.delete_office(db, office_id)
    if deleted_office is None:
        raise HTTPException(status_code=404, detail="Office not found")
    return {"message": "Office deleted successfully"}

 






