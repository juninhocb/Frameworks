from pydantic import BaseModel
from enum import Enum


class Nationality(str, Enum):
    PORTUGUESE = 'br'
    ENGLISH = 'en'
    SPANISH = 'ar'

class OfficeBase(BaseModel):
    name: str

class OfficeCreate(OfficeBase):
    pass

class OfficeUpdate(OfficeBase):
    pass

class Office(OfficeBase):
    id: int

    class Config:
        orm_mode = True

class PersonBase(BaseModel):
    name: str
    age: int
    is_retired: bool
    nationality: Nationality
    id_office: int

class PersonCreate(PersonBase):
    pass

class PersonUpdate(PersonBase):
    pass

class Person(PersonBase):
    id: int
    office: Office

    class Config:
        orm_mode = True