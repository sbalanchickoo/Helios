from flask import Flask
from .config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


# Global DB object
db = SQLAlchemy()
# Global login manager object
login_manager = LoginManager()
application = Config.APPLICATION


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)

    # Help prevent users’ sessions from being stolen
    login_manager.session_protection = "Strong"
    # Redirects any view decorated with login_required to this one, with the next variable set
    login_manager.login_view = "core.sign_in"
    # Associate the login object to current app, so we can use login_required and other features
    login_manager.init_app(app)

    return app
