from flask import Blueprint, request
from http import HTTPStatus

from ..models import Ninja
from ..schema import ninja_schema_list, ninja_schema
from ..services import update


bp_ninja = Blueprint('pb_ninja', __name__)


@bp_ninja.route('/', methods=['GET'])
def listing():
    try:
        ninja_list = Ninja.query.all()

        return ninja_schema_list.dump(ninja_list), HTTPStatus.OK
    except Exception as error:
        return {'msg': str(error)}, HTTPStatus.BAD_REQUEST


@bp_ninja.route('/<int:ninja_id>', methods=['GET'])
def get(ninja_id: int):
    try:
        ninja = Ninja.query.get(ninja_id)
        return ninja_schema.dump(ninja), HTTPStatus.OK

    except Exception as error:
        print(error)
        return {'msg': str(error)}, HTTPStatus.BAD_REQUEST


@bp_ninja.route('/', methods=['POST'])
def create():
    try:
        ninja_body = request.get_json()
        descerialized_ninja = ninja_schema.load(ninja_body)

        descerialized_ninja.save(True)
        return ninja_body, HTTPStatus.CREATED

    except Exception as error:
        print(error)
        return {'msg': str(error)}, HTTPStatus.BAD_REQUEST


@bp_ninja.route('/<int:ninja_id>', methods=['PATCH'])
def update(ninja_id: int):
    try:
        ninja_body = request.get_json()

        updated_ninja = update(ninja_body, Ninja, ninja_id)
        return ninja_schema.dump(updated_ninja), HTTPStatus.OK

    except Exception as error:
        print(error)
        return {'msg': str(error)}, HTTPStatus.BAD_REQUEST
