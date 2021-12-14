from flask_restful import Resource, Api

class Query(Resource):
    def get(self):
        retval = "Query"
        return retval
