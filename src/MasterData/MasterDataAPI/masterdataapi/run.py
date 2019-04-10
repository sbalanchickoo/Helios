from config import config, Config
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    db = SQLAlchemy(app)
    db.create_all()
    db.init_app(app)
    jwt = JWTManager(app)
    return app


