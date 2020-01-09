from flask_restful import reqparse, Resource
from flask import Response
from src.models import User
from src.db import db

parser = reqparse.RequestParser()
parser.add_argument('email', type=str, required=False, help='mail of the user')


class del_user(Resource):
    def post(self):
        args = parser.parse_args(strict=True)
        id_user = User.query.filter_by(email=args['email']).delete()

        db.session.commit()

        return Response(
            response=id_user.to_json(),
            status=200, mimetype='application/json')
