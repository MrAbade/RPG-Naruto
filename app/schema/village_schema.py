from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from ..models import Village


class VillageSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Village
        include_relationships = True
        load_instance = True
