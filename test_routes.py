from flask import Blueprint, jsonify
from flask_login import login_required
from . import mongo

test_routes = Blueprint('test_routes', __name__)


@test_routes.route('/users', methods=['GET'])
@login_required
def get_all_users():
	users = mongo.db.user
	output = []
	for u in users.find():
		output.append({'name': u['name'], 'weight': u['weight'], 'height': u['height']})
	return jsonify({'result': output})


@test_routes.route('/profile', methods=['GET'])
@login_required
def get_profile():
	return 'Hello, you are logged in!'


@test_routes.route('/', methods=['GET'])
def get_index():
	return 'Hello, please log in!'


@test_routes.route('/signup_success', methods=['GET'])
def get_signup_success():
	return 'Signup successful, please log in!'
