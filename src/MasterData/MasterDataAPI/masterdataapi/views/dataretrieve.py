from models.state import State
from models.country import Country
from models.user import User
from flask import url_for


def make_public_country(country):
    new_country = {}
    for field in country:
        if field == 'id':
            new_country['uri'] = url_for('return_country_by_name', country_name=country['country_name'], _external=True)
        else:
            new_country[field] = country[field]
    return new_country


def get_states():
    states = State.query.filter(State.abbrev != '').all()
    return [i.serialize for i in states]


def get_countries():
    countries = Country.query.all()
    response = [make_public_country(i.serialize) for i in countries]
    return response


def get_country_by_currency(currency_code):
    countries = Country.query.filter_by(currency_code=currency_code)
    response = [make_public_country(i.serialize) for i in countries]
    return response


def get_country_by_name(name):
    countries = Country.query.filter_by(country_name=name)
    response = [make_public_country(i.serialize) for i in countries]
    return response


def get_users():
    users = User.query.all()
    response = [i.serialize for i in users]
    return response


def get_user_by_email_password(email, password):
    users = User.query.filter_by(email=email)
    user = [u for u in users if u['password_hash'] == User.verify_password(u, password)]
    response = [i.serialize for i in user]
    if len(response) == 0:
        return 0
    else:
        response
