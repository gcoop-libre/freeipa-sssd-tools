from flask_restful import Resource, Api
from flask import jsonify


class Root(Resource):
    def get(self):
        retval = "freeIPA user's cache clear requests queueing RESTful API"
        return jsonify({"retval": retval})
