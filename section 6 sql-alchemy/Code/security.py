from flask import jsonify
from flask_jwt_extended import create_access_token
from werkzeug.security import safe_str_cmp  # for safely comparing strings instead of '=='

from models.user import UserModel


def authenticate(username, password):
    # If no such username in the dict, return None, else return the dict value
    user = UserModel.find_by_username(username)
    if user and safe_str_cmp(user.password, password):
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token), 200
    return jsonify({"msg": "Bad username or password"}), 401

def identity(payload):
    user_id = payload['identity']
    return UserModel.find_by_id(user_id)