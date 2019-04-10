from flask import make_response, jsonify, request, url_for, Blueprint
from views.data_retrieve import *
from views.dataupsert import *
from flask_jwt_extended import jwt_required

country_route = Blueprint('country', __name__)


def make_public_country(country):
    new_country = {}
    for field in country:
        if field == 'id':
            new_country['uri'] = url_for('country.return_country_by_name', country_name=country['country_name'], _external=True)
        else:
            new_country[field] = country[field]
    return new_country


@country_route.route("/country/currency/<string:currency_code>", methods=['GET'])
def return_country_by_currency(currency_code):
    countries = get_country_by_currency(currency_code)
    response = [make_public_country(i.serialize) for i in countries]
    if len(countries) == 0:
        return make_response(jsonify({'error': 'Not found'}), 404)
    else:
        return jsonify({'countries': response})


@country_route.route("/countries", methods=['GET'])
def return_country_by_name():
    if 'country_name' in request.args:
        countries = get_country_by_name(request.args['country_name'])
    elif 'currency_code' in request.args:
        countries = get_country_by_currency(request.args['currency_code'])
    else:
        countries = get_countries()
    response = [make_public_country(i.serialize) for i in countries]
    return jsonify({'countries': response})


@country_route.route('/country', methods=['POST'])
@jwt_required
def create_country():
    if not request.json or not 'country_name' in request.json or not 'currency_code' in request.json:
        return make_response(jsonify({'error': 'Invalid input'}), 404)
    else:
        country = {
            'currency_code': request.json['currency_code'],
            'country_name': request.json['country_name'],
        }
        add_result = add_country(country)
        if add_result == -1:
            return make_response(jsonify({'error': 'Country already exists'}), 404)
        else:
            countries = [make_public_country(i.serialize) for i in get_countries()]
            country = [c for c in countries if c['country_name'].lower() == request.json['country_name'].lower()]
            if len(country) == 0:
                return make_response(jsonify({'error': 'Not found'}), 404)
            return jsonify({'country': country[0]}), 201
            #return country[0]


@country_route.route('/country', methods=['PUT'])
@jwt_required
def update_country():
    if not request.json or ( \
                    (not 'old_name' in request.json or not 'new_name' in request.json) and \
                    (not 'country_name' in request.json or not 'currency_code' in request.json)):
        return make_response(jsonify({'error': 'Invalid input'}), 404)
    else:
        update_result = update_country_name(old_name=request.json['old_name'], new_name=request.json['new_name'])
        if update_result == -1:
            return make_response(jsonify({'error': 'Country already exists'}), 404)
        else:
            countries = get_countries()
            country = [c for c in countries if c['country_name'].lower() == request.json['new_name'].lower()]
            if len(country) == 0:
                return make_response(jsonify({'error': 'Not found'}), 404)
            return jsonify({'country': country[0]}), 201

