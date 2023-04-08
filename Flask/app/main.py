from flask_migrate import Migrate
from flask import Flask
from app.office.api import api_office_bp
from app.person.api import api_person_bp
from app.dao.database import db

def create_app():
    app = Flask(__name__)
    app.register_blueprint(api_office_bp, name='office_api',  url_prefix='/office')
    app.register_blueprint(api_person_bp, name='person_api', url_prefix='/person')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root@localhost:3306/db_flask'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app) 

    with app.app_context():
        db.create_all()

    return app

app = create_app() 
migrate = Migrate(app, db)
from app.office.models import Office
from app.person.models import Person

if __name__ == '__main__':
    app.run()



