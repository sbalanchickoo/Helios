# Standard library imports

# Third party imports
from flask import Flask
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# Local application imports
from thermos.config import Config


# Global db object that can be used by model classes, will be associated with the app object later
db = SQLAlchemy()

# Global login manager object
login_manager = LoginManager()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    # app.logger.setLevel(DEBUG)
    db.init_app(app)
    moment = Moment(app)

    login_manager.session_protection = "Strong"

    # Redirects any view decorated with login_required to this one, with the next variable set
    login_manager.login_view = "sign_in"

    # Associate the login object to current app, so we can use login_required and other features
    login_manager.init_app(app)

    with app.app_context():
        # Import models and views so that the create all statement will include them
        # from .models import bookmark, user
        # from .views import errors, core_views

        # Create tables for our models
        db.create_all()

    return app

