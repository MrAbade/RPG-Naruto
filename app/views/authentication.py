from flask import Blueprint, request
from flask_jwt_extended import create_access_token, create_refresh_token, fresh_jwt_required, get_jwt_claims
from http import HTTPStatus
from datetime import timedelta

from ..models import User

from ..schema import user_schema

from ..errors import EmailOrPasswordNotReceived
from ..errors import UserNotFound

bp_auth = Blueprint('bp_auth', __name__)


@bp_auth.route('/login', methods=['POST'])
def login():
    try:
        body = request.get_json()

        email = body.get('email')
        password = body.get('password')

        if not email or not password:
            raise EmailOrPasswordNotReceived('You need to pass the email and password')

        found_user = User.query.filter_by(email=email).first()

        if not found_user or not found_user.compare_password(password):
            raise UserNotFound('Email or password is not correct')

        id_user_token = create_access_token(identity=found_user.id, expires_delta=timedelta(days=7))
        id_user_fresh = create_refresh_token(identity=found_user.id, expires_delta=timedelta(days=14))

        return {'access-token': id_user_token, 'fresh-token': id_user_fresh}, 200
    except Exception as error:
        return {'msg': str(error)}, HTTPStatus.BAD_REQUEST


@bp_auth.route('/signup', methods=['POST'])
def signup():
    try:
        body = request.get_json()

        name = body.get('name')
        surname = body.get('surname')
        email = body.get('email')
        password = body.get('password')

        created_user = User(name=name, surname=surname, email=email)
        created_user.save_password(password)
        created_user.save(True)

        return user_schema(created_user), 201
    except Exception as error:
        return {'msg': str(error)}, HTTPStatus.BAD_REQUEST


@bp_auth.route('/refresh', methods=['GET'])
@fresh_jwt_required
def refresh():
    user_id = get_jwt_claims()
    user_id_token = create_access_token(identity=user_id, expires_delta=timedelta(days=7))
    return {'access-token': user_id_token}
