from flask import make_response, jsonify, request, Blueprint
from views.data_retrieve import *
from views.dataupsert import *
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_refresh_token_required, get_jwt_identity

user_route = Blueprint('user', __name__)


@user_route.route("/masterdata/api/v1/users", methods=['GET'])
def return_users():
    users = get_users()
    response = jsonify(users = users)
    return response


@user_route.route("/masterdata/api/v1/user", methods=['POST'])
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


@user_route.route("/masterdata/api/v1/login", methods=['GET'])
def return_user():
    if not request.json \
            or not 'email' in request.json \
            or not 'password' in request.json:
        return make_response(jsonify({'error': 'Invalid input'}), 404)
    else:
        result = get_user_by_email_password(request.json['email'], request.json['password'])
        if result == -1:
            return make_response(jsonify({'error': 'User email or password not found'}), 404)
        elif result == -2:
            return make_response(jsonify({'error': 'User email or password not found'}), 404)
        elif result == -3:
            return make_response(jsonify({'error': 'User email or password not found'}), 404)
        else:
            try:
                access_token = create_access_token(identity=result)
                refresh_token = create_refresh_token(identity=result)
                return jsonify({
                    'user': result,
                    'message': 'User {} was found'.format(result['email']),
                    'access_token': access_token,
                    'refresh_token': refresh_token
                }), 201
            except:
                return make_response(jsonify({'message': 'Something went wrong'}), 500)


@jwt_refresh_token_required
def post(self):
    current_user = get_jwt_identity()
    access_token = create_access_token(identity = current_user)
    return {'access_token': access_token}