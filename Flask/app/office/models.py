from app.dao.models import BaseModel
from app.dao.database import db

class Office(BaseModel):
    __tablename__ = 'office'
    name = db.Column(db.String(30), nullable=False, default="unknown", unique=True)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name
        }