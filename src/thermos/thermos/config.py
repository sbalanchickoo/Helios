# Standard library imports
import os


class Config:
    BASEDIR = os.path.abspath(os.path.dirname(__file__))
    SECRET_KEY = os.environ.get('SECRET_KEY') or "b'|\xec\x08\x8b<\x93m\x11\x03YP\x8a\xcc]\xf5\xc1k]\xf5\xa4""\xd0[\x91'"
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASEDIR, 'thermos.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
