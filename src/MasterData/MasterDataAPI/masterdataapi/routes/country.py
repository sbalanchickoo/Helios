from masterdataapi import app
from flask import make_response, jsonify, request
from views.dataretrieve import *
from views.dataupsert import *
from flask_jwt_extended import jwt_required


@app.route("/masterdata/api/v1/country/currency/<string:currency_code>", methods=['GET'])
def return_country_by_currency(currency_code):
    countries = get_country_by_currency(currency_code)
    if len(countries) == 0:
        return make_response(jsonify({'error': 'Not found'}), 404)
    else:
        return jsonify({'countries': countries})


@app.route("/masterdata/api/v1/countries", methods=['GET'])
@jwt_required
def return_country_by_name():
    if 'country_name' in request.args:
        countries = get_country_by_name(request.args['country_name'])
    elif 'currency_code' in request.args:
        countries = get_country_by_currency(request.args['currency_code'])
    else:
        countries = get_countries()
    return jsonify({'countries': countries})


@app.route('/masterdata/api/v1/country', methods=['POST'])
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
            countries = get_countries()
            country = [c for c in countries if c['country_name'].lower() == request.json['country_name'].lower()]
            if len(country) == 0:
                return make_response(jsonify({'error': 'Not found'}), 404)
            return jsonify({'country': country[0]}), 201


@app.route('/masterdata/api/v1/country', methods=['PUT'])
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

