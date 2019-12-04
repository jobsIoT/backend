from flask_restful import reqparse, Resource
from flask import Response
import json
from src.models import User
from src.db import db

parser = reqparse.RequestParser()
parser.add_argument('firstname', type=str, required=False, help='Name of the user')
parser.add_argument('lastname', type=str, required=False, help='surname of the user')
parser.add_argument('email', type=str, required=False, help='mail of the user')
parser.add_argument('password', type=str, required=False, help='password of ther user')


class Modify_user(Resource):
    def post(self):
        args = parser.parse_args(strict=True)
        id_user = User.query.filter_by(email=args['email']).first()
        if id_user is None:
            return Response(
                response=json.dumps(dict(error='User doesn\'t exist')),
                status=400, mimetype='application/json')

        if args['firstname'] is not None :
            id_user.firstname = args['firstname']
        if args['lastname'] is not None :
            id_user.lastname = args['lastname']
        if args['password'] is not None :
            id_user.password = args['password']

        db.session.commit()

        return Response(
            response=id_user.to_json(),
            status=200, mimetype='application/json')
