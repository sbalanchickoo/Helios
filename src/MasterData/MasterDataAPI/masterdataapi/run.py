from config import config, Config
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

db = SQLAlchemy()

# app = Flask(__name__)
# app.config.from_object(Config)
# db = SQLAlchemy(app)
# db.create_all()
# db.init_app(app)
# jwt = JWTManager(app)


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    db = SQLAlchemy(app)
    db.create_all()
    db.init_app(app)
    jwt = JWTManager(app)
    #from routes.main import index
    return app


#from routes.country import *
#from routes.user import return_users
#from routes.state import return_states
#from routes.main import index