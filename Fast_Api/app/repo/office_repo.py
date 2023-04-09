from sqlalchemy.orm import Session
from domain.models import Office

def get_all_offices(db: Session):
    return db.query(Office).all()

def get_office(db: Session, office_id: int):
    return db.query(Office).filter(Office.id == office_id).first()

def create_office(db, office):
    new_office = Office(name=office.name)
    db.add(new_office)
    db.commit()
    return new_office

def update_office(db, office_id, office):
    db_office = db.query(Office).filter(Office.id == office_id).first()
    if not db_office:
        return None
    db_office.name = office.name
    db.commit()
    return db_office

def delete_office(db, office_id):
    db_office = db.query(Office).filter(Office.id == office_id).first()
    if not db_office:
        return None
    db.delete(db_office)
    db.commit()
    return db_office