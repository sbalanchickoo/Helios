from config import Config
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
db.create_all()
db.init_app(app)
jwt = JWTManager(app)


from routes.country import *
from routes.user import return_users
from routes.state import return_states
from routes.main import index