from flask import Flask
from flask_jwt_extended import JWTManager


def config_jwt(app: Flask):
    JWTManager(app)
