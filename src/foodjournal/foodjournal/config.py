import os


class Config():
    SECRET_KEY = "b'bg\xbe\xfa\xd4\xee0\xa1)\xa9\xa1\xd7r\xeb\xc8\xe0\x86\xb0\xa39\xee\xdd(D'"
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    APPLICATION = 'Food Journal'
    SQLALCHEMY_DATABASE_URI = 'sqalchemy:///' + os.path.join(BASE_DIR, 'foodjournal.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True
