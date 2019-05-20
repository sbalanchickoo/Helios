from models.country import Country
from models.user import User
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound


def get_countries():
    """
    Get all countries

    Returns
    -------
    countries
        List of all countries

    """
    countries = Country.query.all()
    return countries


def get_country_by_currency(currency_code):
    """
    Get list of countries filtered by currency code

    Parameters
    ----------
    currency_code
        Country's currency code

    Returns
    -------
    countries
        List of countries with specified currency code

    """
    countries = Country.query.filter_by(currency_code=currency_code)
    return countries


def get_country_by_name(name):
    """
    Get list of countries filtered by name

    Parameters
    ----------
    name
        country name

    Returns
    -------
    country
        unserialized list of all countries

    """
    country = Country.query.filter_by(country_name=name)
    return country


def get_users():
    """
    Get all users

    Returns
    -------
    response
        List of all users

    """
    users = User.query.all()
    response = [i.serialize for i in users]
    return response


def get_user_by_email_password(email, password):
    """
    Get user filtered by email and password

    Parameters
    ----------
    email
        user email address
    password
        user password

    Returns
    -------
    response
        If user exists, return user including JWT tokens
        If user does not exist, return error message

    """
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
