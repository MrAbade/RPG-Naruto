from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, fields

from ..models import Village
from . import NinjaSchema


class VillageSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Village
        include_relationships = True
        load_instance = True
    
    ninjas = fields.Nested(NinjaSchema())
