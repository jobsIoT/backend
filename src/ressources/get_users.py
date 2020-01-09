import json
from flask_restful import Resource
from flask import Response
from src.models import User


class getUsers(Resource):
    def post(self):
        id_ = User.query.all()
        print(id_)
        if id_ is None:
            return Response(
                response=json.dumps(dict(error='User doesn\'t exist')),
                status=400, mimetype='application/json')
        return Response(
                response=bytearray(id_),
                status=200, mimetype='application/json')
