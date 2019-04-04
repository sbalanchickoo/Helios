from models.state import State
from models.country import Country
from models.user import User
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound


def get_states():
    states = State.query.filter(State.abbrev != '').all()
    return [i.serialize for i in states]


def get_countries():
    countries = Country.query.all()
    return countries


def get_country_by_currency(currency_code):
    countries = Country.query.filter_by(currency_code=currency_code)
    return countries


def get_country_by_name(name):
    countries = Country.query.filter_by(country_name=name)
    return countries


def get_users():
    users = User.query.all()
    response = [i.serialize for i in users]
    return response


def get_user_by_email_password(email, password):
    try:
        user = User.query.filter_by(email=email).one_or_none()
        if not user.verify_password(password):
            response = "Password mismatch"
        else:
            response = user.serialize
    except NoResultFound as error:
        response = "Email not found"
    except MultipleResultsFound as error:
        response = "Multiple emails found"

    return response
