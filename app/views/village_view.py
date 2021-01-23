from flask import Blueprint, request
from http import HTTPStatus

from ..models import Village
from ..schema import village_schema_list, village_schema


bp_village = Blueprint('bp_village', __name__)


@bp_village.route('/', methods=['GET'])
def list_villages():
    try:
        village_list = Village.query.all()
        return village_schema_list.dump(village_list), HTTPStatus.OK

    except Exception as error:
        print(error)
        return {'msg': str(error)}, HTTPStatus.BAD_REQUEST


@bp_village.route('/', methods=['POST'])
def create_village():
    try:
        village_body = request.get_json()
        village = Village(name=village_body['name'])
        village.save(True)

        return village_schema.dump(village), HTTPStatus.CREATED

    except Exception as error:
        print(error)
        return {'msg': str(error)}, HTTPStatus.BAD_REQUEST
