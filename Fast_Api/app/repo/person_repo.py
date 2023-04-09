from sqlalchemy.orm import Session
from domain.models import Person

def get_people(db: Session):
    return db.query(Person).all()

def get_person(db: Session, person_id: int):
    return db.query(Person).filter(Person.id == person_id).first()

def create_person(db, person):
    new_office = Person(
        name=person.name,
        age=person.age,
        is_retired=person.is_retired,
        nationality=person.nationality,
        id_office=person.id_office)
    db.add(new_office)
    db.commit()
    return new_office

def update_person(db, person_id, person):
    db_person = db.query(Person).filter(Person.id == person_id).first()
    if not db_person:
        return None
    db_person.name = person.name
    db_person.age  = person.age
    db_person.is_retired = person.is_retired
    db_person.nationality = person.nationality
    db_person.id_office = person.id_office
    db.commit()
    return db_person

def delete_person(db, person_id):
    db_person = db.query(Person).filter(Person.id == person_id).first()
    if not db_person:
        return None
    db.delete(db_person)
    db.commit()
    return db_person