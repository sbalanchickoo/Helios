# Standard library imports

# Third party imports
from flask_login import UserMixin
from sqlalchemy import func
from passlib.hash import bcrypt
from werkzeug.security import check_password_hash, generate_password_hash

# Local application imports
from strand import db


# Flask login requires User class to implement a few methods.
# UserMixin provides default implementations
class User(db.Model, UserMixin):
    __tablename__ = 'User'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)
    password_hash = db.Column(db.String(255), nullable=False)

    # backref can be anything, either the class name or table name
    weight_rel = db.relationship('MetricsLog', backref='user', lazy='dynamic')
    blood_pressure_rel = db.relationship('BloodPressureLog', backref='User', lazy='dynamic')

    #def __repr__(self):
    #    return "<User %r>" % self.username

    @property
    def password(self):
        raise AttributeError('password: Write-only field')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    @staticmethod
    def get_by_username(username):
        return User.query.filter(func.lower(User.username) == func.lower(username)).first()

    @property
    def serialize(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email
        }

    # Not used
    @staticmethod
    def hash_password(password):
        return bcrypt.using(rounds=13).hash(password)

    # Not used
    def verify_password(self, password):
        return bcrypt.verify(password, self.password_hash)
