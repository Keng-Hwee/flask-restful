from flask import Flask, request, jsonify
from flask_restful import Api
from flask_jwt_extended import JWTManager

from security import authenticate
from user import UserRegister
from item import Item, ItemList

app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True
api = Api(app)

# Setup flask-jwt-extended
app.config['JWT_SECRET_KEY'] = 'kh'
jwt = JWTManager(app)  # creates a new endpoint: /auth


# Provide a method to create access tokens. The create_access_token()
# function is used to actually generate the token, and you can return
# it to the caller however you choose.
@app.route('/auth', methods=['POST'])
def login():
    if not request.is_json:
        return jsonify({"msg": "Missing JSON in request"}), 400

    username = request.json.get('username', None)
    password = request.json.get('password', None)
    if not username:
        return jsonify({"msg": "Missing username parameter"}), 400
    if not password:
        return jsonify({"msg": "Missing password parameter"}), 400

    return authenticate(username, password)


api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    app.run(port=5000, debug=True)
