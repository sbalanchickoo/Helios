# Third party imports
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Local application imports
from thermos.config import Config

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    # app.logger.setLevel(DEBUG)
    db.init_app(app)
    with app.app_context():
        # Imports
        from .models import bookmark, user
        from .views import errors, core_views
        # Create tables for our models
        db.create_all()

    return app

