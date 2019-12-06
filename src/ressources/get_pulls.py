from flask_restful import reqparse, Resource
from flask import Response
import json
from src.models import Cardiaque

parser = reqparse.RequestParser()
parser.add_argument('email', type=str, required=True, help='mail of the user you want the information')


class getPulls(Resource):
    def post(self):
        args = parser.parse_args(strict=True)
        pulls = Cardiaque.query.filter_by(email=args['email']).all()

        if pulls is None:
            return Response(
                response=json.dumps(dict(error='User doesn\'t exist')),
                status=400, mimetype='application/json')
        tmp = {i: pulls[i] for i in range(0, len(pulls))}
        return Response(
            response=tmp.to_json(),
            status=200, mimetype='application/json')
