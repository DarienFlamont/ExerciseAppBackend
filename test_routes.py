from flask import Blueprint, jsonify
from . import mongo

test_routes = Blueprint('test_routes', __name__)


@test_routes.route('/users', methods=['GET'])
def get_all_users():
	users = mongo.db.users
	output = []
	for u in users.find():
		output.append({'name' : u['name'], 'weight' : u['weight'], 'height' : u['height']})
	return jsonify({'result': output})
