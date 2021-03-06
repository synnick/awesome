from flask_jwt import JWT

from awesome.models.users import Users


def authenticate(username, password):
    user = Users.query.filter_by(username=username).first()
    if user and user.check_password(password):
        return user


def identity(payload):
    user_id = payload['identity']
    return Users.query.filter_by(id=user_id).first()


jwt = JWT(None, authenticate, identity)
