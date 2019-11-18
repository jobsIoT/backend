from flask_restful import Resource
from flask import Response
import json

class Home(Resource):
    def get(self):

        return Response(response=json.dumps(dict(msg='Hello World')) ,status=200, mimetype='application/json')
