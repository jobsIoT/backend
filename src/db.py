from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from src.config import Config

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config.from_object(Config)
db = SQLAlchemy()
db.init_app(app)

cors = CORS(app, resources={r"*": {"origins": "*"}})
api = Api(app)



def create_app():
    with app.app_context():
        db.create_all()
    return app

def recreate_database():
    with app.app_context():
        db.drop_all()
        db.create_all()
