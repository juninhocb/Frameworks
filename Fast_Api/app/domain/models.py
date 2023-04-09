from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from enum import Enum
from .database import Base


class Nationality(Enum):
    PORTUGUESE = 'pt'
    ENGLISH = 'en'
    SPANISH = 'es'

class BaseModel(Base):
    __abstract__ = True
    id = Column(Integer, primary_key=True)


class Office(BaseModel):
    __tablename__ = 'office'
    name = Column(String(30), nullable=False, default="unknown", unique=True)


class Person(BaseModel):
    __tablename__ = 'person'
    name = Column(String(50), nullable=False, default="unknown", unique=True)
    age = Column(Integer, nullable=False, default=0)
    is_retired = Column(Boolean, nullable=False, default=False)
    nationality = Column(String, nullable=False, default=Nationality.PORTUGUESE)
    id_office = Column(Integer, ForeignKey('office.id'), nullable=False)
    office = relationship('Office', backref='people')