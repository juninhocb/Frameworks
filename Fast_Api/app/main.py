from fastapi import FastAPI
from api import hello_api, office_api, person_api
from domain.database import create_db 

app = FastAPI()

app.include_router(hello_api.router, prefix='/hello')
app.include_router(office_api.router, prefix='/office')
app.include_router(person_api.router, prefix='/person')

create_db()