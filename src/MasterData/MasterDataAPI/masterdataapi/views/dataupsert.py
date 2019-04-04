from models.country import Country
from models.user import User


def add_country(country):
    result = Country.query.all()
    response = [i.serialize for i in result]
    country_check = [c for c in response if c['country_name'].lower() == country['country_name'].lower()]
    if len(country_check) != 0:
        return -1
    else:
        new_country = Country(currency_code=country['currency_code'], country_name=country['country_name'])
        status = Country.add_country(new_country)
        return status


def update_country_name(old_name, new_name):
    """ Update the country name.

    >>> update_country_name("a", "b")
    0

    Parameters
    ----------
    old_name : string
        Original name of country
    new_name : string
        New name of country

    Returns
    -------
    status : int
        update from SQLAlchemy

    """
    result = Country.query.all()
    response = [i.serialize for i in result]
    country_check = [c for c in response if c['country_name'].lower() == old_name.lower()]
    if len(country_check) == 0:
        return -1
    else:
        country_check = [c for c in response if c['country_name'].lower() == new_name.lower()]
        if len(country_check) != 0:
            return -2
        else:
            status = Country.update_country_name(old_name=old_name, new_name=new_name)
            return status


def add_user(user):
    result = User.query.all()
    response = [i.serialize for i in result]
    user_check = [c for c in response if c['email'].lower() == user['email'].lower()]
    if len(user_check) != 0:
        return -1
    else:
        hash = User.hash_password(user['password'])
        new_user = User(first_name=user['first_name'], last_name=user['last_name'], email=user['email'], password_hash=hash)
        status = User.add_user(new_user)
        return status
