# Standard library imports
import os


class Config:
    BASEDIR = os.path.abspath(os.path.dirname(__file__))
    SECRET_KEY = os.environ.get('SECRET_KEY') or "b'\x84\xc2\xc0x\xaeA\\\xf5\xc8e\x7f3\x84[\xa2?'"
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASEDIR, 'strand.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True
    APPLICATION = 'Strand'
