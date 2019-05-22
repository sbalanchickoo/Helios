from config import Config
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    with app.app_context():
        # Imports
        from models import bookmark, user
        # Create tables for our models
        db.create_all()

    return app


