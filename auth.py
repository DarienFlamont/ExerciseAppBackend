from flask import Blueprint, request, redirect, url_for
from flask_login import login_user, logout_user, login_required
from pymongo import DESCENDING
from .helpers import generate_password_hash, check_hashed_password
from .models import User

auth = Blueprint("auth", __name__)


@auth.route('/login', methods=['POST'])
def post_login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    # TODO: Figure out if we need this line or not, for now just pass true into login anyways
    # remember = True if data.get('remember') else False

    user = None
    hashed_password = ''
    try:
        user = User.objects.get({'email': email})
        hashed_password = user.hashed_password
        email_exists = True

        # TODO: Implement a non-buggy way to check if user is already logged in, and redirect them if so
    except User.DoesNotExist:
        email_exists = False

    if not email_exists or not check_hashed_password(password, hashed_password):
        return 'Login Failed, check email or password'

    login_user(user, remember=True)
    return redirect(url_for('test_routes.get_profile'))


@auth.route('/signup', methods=['POST'])
def post_signup():

    data = request.get_json()
    email = data.get('email')
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    password = data.get('password')
    hashed_password = generate_password_hash(password).decode()

    try:
        user = User.objects.get({'email': email})
        email_exists = True
    except User.DoesNotExist:
        email_exists = False

    # TODO: Properly handle the case where email already exists in the database
    #  by throwing a specific HTTP code for user already exists
    if email_exists:
        return 'User already exists'

    # Create a user and write it to the db
    query_set = User.objects.all()
    id_ordering = [('_id', DESCENDING)]
    cursor = query_set.order_by(id_ordering)
    try:
        new_id = int(cursor.first().get_id()) + 1
    except User.DoesNotExist:
        new_id = 0
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
    return redirect(url_for('test_routes.get_signup_success'))


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return 'Logout'
