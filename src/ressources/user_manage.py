from flask_restful import reqparse, Resource
from flask import Response
import json
from src.models import User

parser = reqparse.RequestParser()
parser.add_argument('email', type=str, required=True, help='mail of the user you want the information')


class User_manage(Resource):
    def post(self):
        args = parser.parse_args(strict=True)
        id_user = User.query.filter_by(email=args['email']).first()

        if id_user is None:
            return Response(
                response=json.dumps(dict(error='User doesn\'t exist')),
                status=400, mimetype='application/json')
        return Response(
            response=id_user.to_json(),
            status=200, mimetype='application/json')
