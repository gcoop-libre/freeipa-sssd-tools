import os
from flask import Flask
from flask_restful import Api, reqparse, abort, Resource


def create_app(test_config=None):
    """
    Create and configure the app
    """
    app = Flask(__name__, instance_relative_config=True)
    Api(app)
    with app.app_context():
        if test_config is None:
            app.config.from_pyfile("config/settings.py")
        else:
            app.config.from_pyfile(test_config)

    return app
