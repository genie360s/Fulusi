from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import Config

db = SQLAlchemy()

def create_app():
    api_app = Flask(__name__)
    api_app.config.from_object(Config)
    db.init_app(api_app)

    with api_app.app_context():
        from . import routes, models
        db.create_all()

    return api_app
