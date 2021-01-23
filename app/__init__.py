__version__ = '0.1.0'

from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from dynaconf import FlaskDynaconf

from app.configs import config_db


def create_app(config='production'):
    app = Flask(__name__)
    FlaskDynaconf(app, settings_files=["settings.toml", ".secrets.toml"])

    CORS(app)

    config_db(app)
    Migrate(app, app.db)

    return app
