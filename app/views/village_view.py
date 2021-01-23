from flask import Blueprint, request

from ..models import Village
from ..schema import village_schema_list, village_schema


bp_village = Blueprint('bp_village', __name__)


@bp_village.route('/', methods=['GET'])
def list_villages():
    try:
        village_list = Village.query.all()
        return village_schema_list.dump(village_list), 200

    except Exception as error:
        print(error)
        return {'msg': error.message}, 400


@bp_village.route('/', methods=['POST'])
def create_village():
    try:
        village_body = request.get_json()
        village = Village(name=village_body['name'])
        village.save(True)

        return village_schema.dump(village), 201

    except Exception as error:
        print(error)
        return {'msg': error.message}, 400
