from .village_schema import VillageSchema
village_schema_list = VillageSchema(many=True)
village_schema = VillageSchema()

from .ninja_schema import NinjaSchema
ninja_schema_list = NinjaSchema(many=True)
ninja_schema = NinjaSchema()

from .user_schema import UserSchema
user_schema_list = UserSchema(many=True)
user_schema = UserSchema()
