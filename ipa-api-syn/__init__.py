import os
from flask import Flask
from flask_restful import Api, reqparse, abort, Resource


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    Api(app)
    with app.app_context():
        app.config.from_pyfile("config/settings.py")

    return app
