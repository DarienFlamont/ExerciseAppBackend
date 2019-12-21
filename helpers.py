from bcrypt import hashpw, gensalt, checkpw


# TODO: Define error behaviour, catch exceptions if hashpw throws any, etc
def generate_password_hash(password):
    salt = gensalt()
    return hashpw(password.encode('utf-8'), salt)


def check_hashed_password(password, hashed_password):
    return checkpw(password, hashed_password)
