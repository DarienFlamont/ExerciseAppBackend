from flask import Blueprint
from flask_login import login_required

test_routes = Blueprint('test_routes', __name__)


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
