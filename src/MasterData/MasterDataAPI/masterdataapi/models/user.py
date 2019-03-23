from run import db
import datetime
from passlib.hash import bcrypt


class User(db.Model):
    """ User Model for storing user related details """
    __tablename__ = "User"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(128), unique=False, nullable=False)
    last_name = db.Column(db.String(128), unique=False, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)

    def __init__(self, first_name, last_name, email, password_hash, admin=False):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password_hash = password_hash
        self.registered_on = datetime.datetime.now()
        self.admin = admin

    def add_user(new_user):
        db.session.add(new_user)
        db.session.commit()
        return 1

    def hash_password(password):
        return bcrypt.using(rounds=13).hash(password)

    def verify_password(self, password):
        return bcrypt.verify(password, self.password_hash)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'password_hash': self.password_hash
        }