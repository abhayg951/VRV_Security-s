from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity, get_jwt
from .models import User, Role

auth_blueprint = Blueprint('auth', __name__)

@auth_blueprint.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    if "username" not in data:
        return jsonify({'message': 'Username is required'}), 400
    if "password" not in data:
        return jsonify({'message': 'Password is required'}), 400
    if User.find_user_by_username(data['username']):
        return jsonify({'message': 'User already exists'}), 400
    User.create_user(data['username'], data['password'])
    return jsonify({'message': 'User registered successfully'}), 201

@auth_blueprint.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    if "username" not in data:
        return jsonify({'message': 'Username is required'}), 400
    if "password" not in data:
        return jsonify({'message': 'Password is required'}), 400
    user = User.find_user_by_username(data['username'])
    if user and User.verify_password(user["password"], data['password']):
        access_token = create_access_token(identity=user['username'], additional_claims={'role': user['role']})
        return jsonify(access_token=access_token), 200
    return jsonify({'message': 'Invalid credentials'}), 401

@auth_blueprint.route('/me', methods=['GET'])
@jwt_required()
def get_user_info():
    current_user = get_jwt_identity()
    print(current_user)
    claims = get_jwt()
    user = User.find_user_by_username(current_user)
    return jsonify({'username': user['username'], 'role': claims['role']}), 200