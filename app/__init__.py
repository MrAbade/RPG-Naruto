__version__ = '0.1.0'

from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate

from config import config_selector
from app.configs import config_db


def create_app(config='production'):
    app = Flask(__name__)
    app.config.from_object(config_selector[config])

    CORS(app)

    config_db(app)
    Migrate(app, app.db)

    return app
