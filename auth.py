from flask import Blueprint, request, jsonify
from . import mongo
from .helpers import generate_password_hash, check_hashed_password

auth = Blueprint("auth", __name__)


@auth.route('/login')
def login():
    return 'Login'


@auth.route('/signup', methods=['POST'])
def signup_post():
    data = request.get_json()
    email = data.get('email')
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    password = data.get('password')

    email_exists = mongo.db.users.count_documents({'email': email}) > 0

    # TODO: Properly handle the case where email already exists in the database
    #  (further error handling)
    if email_exists:
        return 'User already exists'

    # Create a user and write it to the db
    # TODO: Generate password hash
    # TODO: Create MongoDB user model - Darien is doing this
    mongo.db.users.insert_one({
        'email': email,
        'first_name': first_name,
        'last_name': last_name,
        'password': generate_password_hash(password)
    })
    return 'Signup successful'


@auth.route('/logout')
def logout():
    return 'Logout'