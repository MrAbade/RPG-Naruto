from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from ..models import Ninja


class NinjaSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Ninja
        include_relationships = True
        load_instance = True
