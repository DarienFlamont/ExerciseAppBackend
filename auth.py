from flask import Blueprint, request
from flask_login import login_user
from . import mongo
from .models import User
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

    email_exists = mongo.db.user.count_documents({'email': email}) > 0
    user = None
    hashed_password = ''
    if email_exists:
        # TODO: the user is guaranteed to be there, but maybe there's a cleaner way to access the first one
        user_dict = mongo.db.user.find({'email': email})[0]
        hashed_password = user_dict.get('hashed_password')
        user = User(
            id=user_dict.get('id'),
            first_name=user_dict.get('first_name'),
            last_name=user_dict.get('last_name'),
            email=user_dict.get('email'),
            hashed_password=hashed_password,
            height_inches=user_dict.get('height_inches'),
            weight_lbs=user_dict.get('weight_lbs')
        )

    if not email_exists or not check_hashed_password(password, hashed_password):
        return 'Login Failed, check email or password'

    login_user(user, remember=remember)
    return 'Login successful'


@auth.route('/signup', methods=['POST'])
def signup_post():
    data = request.get_json()
    email = data.get('email')
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    password = data.get('password')
    hashed_password = generate_password_hash(password).decode()

    email_exists = mongo.db.user.count_documents({'email': email}) > 0

    # TODO: Properly handle the case where email already exists in the database
    #  (further error handling)
    if email_exists:
        return 'User already exists'

    # Create a user and write it to the db
    from .models import User
    # TODO: Use a cached max current userID instead of count, this is vulnerable to deletes
    #  this line below is getting closer, but may need to optimize later
    # new_id = mongo.db.user.find().sort({'id': -1}).limit(1) + 1
    new_id = mongo.db.user.count()
    # TODO: Height and weight shouldn't always be 0 obviously
    User(
        id=new_id,
        first_name=first_name,
        last_name=last_name,
        email=email,
        hashed_password=hashed_password,
        height_inches=0,
        weight_lbs=0
    ).save()
    return 'Signup successful'


@auth.route('/logout')
def logout():
    return 'Logout'