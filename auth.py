from flask import Blueprint, request, jsonify
from . import mongo
from .helpers import generate_password_hash, check_hashed_password

auth = Blueprint("auth", __name__)


@auth.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    # not exactly sure what we're remembering here, maybe something to do with the case
    # where the user closes the browser?
    remember = True if data.get('remember') else False

    email_exists = mongo.db.users.count_documents({'email': email}) > 0
    hashed_password = ''
    if email_exists:
        # it's guaranteed to be there, but maybe there's a cleaner way to access the first one
        hashed_password = mongo.db.users.find({'email': email})[0]['hashed_password']

    if not email_exists or not check_hashed_password(password, hashed_password):
        return 'Login Failed, check email or password'

    return 'Login successful'


@auth.route('/signup', methods=['POST'])
def signup_post():
    data = request.get_json()
    email = data.get('email')
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    password = data.get('password')
    hashed_password = generate_password_hash(password).decode()

    email_exists = mongo.db.users.count_documents({'email': email}) > 0

    # TODO: Properly handle the case where email already exists in the database
    #  (further error handling)
    if email_exists:
        return 'User already exists'

    # Create a user and write it to the db
    mongo.db.users.insert_one({
        'email': email,
        'first_name': first_name,
        'last_name': last_name,
        'hashed_password': hashed_password
    })
    return 'Signup successful'


@auth.route('/logout')
def logout():
    return 'Logout'