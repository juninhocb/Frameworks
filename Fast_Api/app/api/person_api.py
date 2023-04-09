from fastapi import APIRouter, Depends, HTTPException, Response
from domain.schemas import PersonCreate, PersonUpdate
from domain.database import get_db
from sqlalchemy.orm import Session
from repo import person_repo

router  = APIRouter()

@router.get("/read")
def get_people(db: Session = Depends(get_db)):
    people = person_repo.get_people(db)
    if people is None:
        raise HTTPException(status_code=404, detail="People not found")
    return people

@router.get("/read/{person_id}")
def get_person(person_id: int, db: Session = Depends(get_db)):
    person = person_repo.get_person(db, person_id)
    if person is None:
        raise HTTPException(status_code=404, detail="Person not found")
    return person 

@router.post("/create")
def create_person(person: PersonCreate, db: Session = Depends(get_db)):
    created_person = person_repo.create_person(db, person)
    response = Response(status_code=201)
    response.headers["Location"] = f"/person/read/{created_person.id}"
    return response


@router.put("/update/{person_id}")
def update_person(person_id: int, person: PersonUpdate, db: Session = Depends(get_db)):
    update_person = person_repo.update_person(db, person_id, person)
    if update_person is None:
        raise HTTPException(status_code=404, detail="Person not found")
    return {"message": "Person updated successfully"}


@router.delete("/delete/{person_id}")
def delete_person(person_id: int, db: Session = Depends(get_db)):
    deleted_person = person_repo.delete_person(db, person_id)
    if deleted_person is None:
        raise HTTPException(status_code=404, detail="Person not found")
    return {"message": "Person deleted successfully"}

 






