from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from api.root import Root
from api.sync import Sync
from api.query import Query

app = Flask(__name__)
api = Api(app)

api.add_resource(Root,'/','/syn','/qry')
api.add_resource(Sync,'/syn/<string:userid>')
api.add_resource(Query,'/qry/<string:userid>')
