from flask import Flask
from flask_restful import Api
from api.root import Root
from api.sync import Sync
from api.query import Query

"""
IPA-API-SYN endpoint definitions
"""

app = Flask(__name__)
api = Api(app)

qry_routes = [
    "/qry/<string:userid>",
    "/qry/<string:userid>/<int:recordnum>",
]

api.add_resource(Root, "/", "/syn", "/qry")
api.add_resource(Sync, "/syn/<string:userid>")
api.add_resource(Query, *qry_routes)
