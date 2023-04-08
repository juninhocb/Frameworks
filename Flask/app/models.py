from .database import db
from .enums import Nationality

class BaseModel(db.Model):
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True)

class Office(BaseModel):
    __tablename__ = 'office'
    name = db.Column(db.String(30), nullable=False, default="unknown", unique=True)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name
        }

class Person(BaseModel):
    __tablename__ = 'person'
    name = db.Column(db.String(50), nullable=False, default="unknown", unique=True)
    age = db.Column(db.Integer, nullable=False, default=0)
    is_retired = db.Column(db.Boolean, nullable=False, default=False)
    nationality = db.Column(db.Enum(Nationality), nullable=False, default=Nationality.PORTUGUESE)
    id_office = db.Column(db.Integer, db.ForeignKey('office.id'), nullable=False)
    office = db.relationship('Office', backref='people')

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'is_retired': self.is_retired,
            'nationality': self.nationality.name,
            'id_office' : self.id_office, 
            'office' : self.office.to_json()
        }



