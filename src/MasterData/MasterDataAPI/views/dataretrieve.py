from models.state import USState
from models.country import Country
from flask import jsonify


def get_state():
    states = USState.query.filter(USState.abbrev != '').all()
    return jsonify([i.serialize for i in states])


def get_country():
    countries = Country.query.all()
    return jsonify([i.serialize for i in countries])
