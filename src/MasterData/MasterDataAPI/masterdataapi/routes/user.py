from masterdataapi import app
from flask import make_response, jsonify, request
from views.dataretrieve import *
from views.dataupsert import *
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, jwt_refresh_token_required, get_jwt_identity, get_raw_jwt


@app.route("/masterdata/api/v1/users", methods=['GET'])
def return_users():
    users = get_users()
    response = jsonify(users = users)
    return response


@app.route("/masterdata/api/v1/user", methods=['POST'])
def create_user():
    if not request.json \
            or not 'first_name' in request.json \
            or not 'last_name' in request.json \
            or not 'email' in request.json \
            or not 'password' in request.json:
        return make_response(jsonify({'error': 'Invalid input'}), 404)
    else:
        user = {
            'first_name': request.json['first_name'],
            'last_name': request.json['last_name'],
            'email': request.json['email'],
            'password': request.json['password']
        }
        add_result = add_user(user)
        if add_result == -1:
            return make_response(jsonify({'error': 'User already exists'}), 404)
        else:
            users = get_users()
            user = [c for c in users if c['email'].lower() == request.json['email'].lower()]
            if len(user) == 0:
                return make_response(jsonify({'error': 'Not found'}), 404)
            else:
                user = user[0]
                try:
                    access_token = create_access_token(identity=user['email'])
                    refresh_token = create_refresh_token(identity=user['email'])
                    return jsonify({
                        'user': user['email'],
                        'message': 'User {} was created'.format(user['email']),
                        'access_token': access_token,
                        'refresh_token': refresh_token
                    }), 201
                except:
                    return make_response(jsonify({'message': 'Something went wrong'}), 500)


@app.route("/masterdata/api/v1/user", methods=['GET'])
def return_user():
    if not request.json \
            or not 'email' in request.json \
            or not 'password' in request.json:
        return make_response(jsonify({'error': 'Invalid input'}), 404)
    else:
        user = {
            'email': request.json['email'],
            'password': request.json['password']
        }
        result = get_user_by_email_password(user)
        if result == -1:
            return make_response(jsonify({'error': 'User not found'}), 404)
        else:
            users = get_user_by_email_password(user)
            user = [c for c in users if c['email'].lower() == request.json['email'].lower()]
            if user == 0:
                return make_response(jsonify({'error': 'Not found'}), 404)
            # return jsonify({'user': user[0]}), 201
            else:
                try:
                    access_token = create_access_token(identity=user['email'])
                    refresh_token = create_refresh_token(identity=user['email'])
                    return jsonify({
                        'user': user[0],
                        'message': 'User {} was found'.format(user['email']),
                        'access_token': access_token,
                        'refresh_token': refresh_token
                    }), 201
                except:
                    return {'message': 'Something went wrong'}, 500
