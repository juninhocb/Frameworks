from flask_migrate import Migrate
from flask import Flask
from .api import api_bp
from .database import db

def create_app():
    app = Flask(__name__)
    app.register_blueprint(api_bp, url_prefix='/api')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root@localhost:3306/db_flask'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app) 

    with app.app_context():
        db.create_all()

    return app

app = create_app() 
migrate = Migrate(app, db)
from .models import * 

if __name__ == '__main__':
    app.run()



