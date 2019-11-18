import json
from flask_restful import reqparse, Resource
from flask import Response
from src.models import User

parser = reqparse.RequestParser()
parser.add_argument('mail', type=str, required=True, help='mail of the user')
parser.add_argument('password', type=str, required=True, help='password of ther user')


class Connexion(Resource):
    def post(self):
        args = parser.parse_args(strict=True)
        id_ = User.query.filter_by(email=args['mail']).first()
        if id_ is None:
            return Response(
                response=json.dumps(dict(error='User doesn\'t exist')),
                status=400, mimetype='application/json')
        if id_.password != args['password']:
            return Response(
                response=json.dumps(dict(error='Wrong password')),
                status=400, mimetype='application/json')
        return Response(
                response=id_.to_json(),
                status=200, mimetype='application/json')
