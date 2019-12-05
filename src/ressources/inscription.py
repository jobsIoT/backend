from flask_restful import reqparse, Resource
import json
from flask import Response
from src.db import db
from src.models import User

parser = reqparse.RequestParser()
parser.add_argument('email', type=str, required=True, help='mail of the user')
parser.add_argument('firstname', type=str, required=True, help='Error : Name of the user')
parser.add_argument('lastname', type=str, required=True, help='surname of the user')
parser.add_argument('password', type=str, required=True, help='password of ther user')
parser.add_argument('isPremium', type=bool, required=True, help='is a premium user')


class Inscription(Resource):
    def post(self):
        args = parser.parse_args(strict=True)
        new_user = User(firstname=args['firstname'], lastname=args['lastname'], email=args['email'],
                        password=args['password'], isPremium=args['isPremium'])
        id_ = User.query.filter_by(email=args['email']).first()
        if id_ is not None:
            return Response(
                response=json.dumps(dict(error='user exist already')),
                status=400, mimetype='application/json')
        db.session.add(new_user)
        db.session.commit()
        id_ = User.query.filter_by(email=args['email']).first()
        return Response(
                response=id_.to_json(),
                status=200, mimetype='application/json')
