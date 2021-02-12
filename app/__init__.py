__version__ = '0.1.3'

from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from dynaconf import FlaskDynaconf

from app.configs import config_db
from app.configs import config_jwt
from app.views import config_views


def create_app(config='production'):
    app = Flask(__name__)
    FlaskDynaconf(app, settings_files=["settings.toml", ".secrets.toml"])

    CORS(app)

    config_db(app)
    Migrate(app, app.db)
    
    config_jwt(app)
    config_views(app)

    return app
