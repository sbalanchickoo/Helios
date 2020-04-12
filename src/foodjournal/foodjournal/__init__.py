from flask import Flask
from .config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
application = Config.APPLICATION
# login_manager = LoginManager()
# login_manager.session_protection = 'Strong'
# login_manager.login_view = "core.sign_in"


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    # login_manager.init_app(app)

    return app