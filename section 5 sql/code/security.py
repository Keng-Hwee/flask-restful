from flask import request, jsonify
from flask_jwt_extended import create_access_token
from werkzeug.security import safe_str_cmp  # for safely comparing strings instead of '=='

from user import User

users = [
    User(1, 'bob', 'asdf')
]

username_mapping = {u.username: u for u in users}
userid_mapping = {u.id: u for u in users}


def authenticate(username, password):
    # If no such username in the dict, return None, else return the dict value
    user = username_mapping.get(username, None)
    if user and safe_str_cmp(user.password, password):
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token), 200
    return jsonify({"msg": "Bad username or password"}), 401

