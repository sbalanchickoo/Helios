import os
import datetime

class Config(object):
    BASEDIR = os.path.abspath(os.path.dirname(__file__))
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'mysql+pymysql://root:sb@mysql/MasterData'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'mysql+pymysql://root:sb@localhost/MasterData'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = 'jwt-secret-string'
    JWT_ACCESS_TOKEN_EXPIRES = datetime.timedelta(minutes=1)

#db.init_app(app)
# config - run - mda
# config - models - views - mda
# run - models