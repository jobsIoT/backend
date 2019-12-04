import datetime
from flask_restful import reqparse, Resource
from flask import Response
from src.models import Cardiaque
from src.db import db

parser = reqparse.RequestParser()
parser.add_argument('pulls', type=str, required=True, help='the cardiac pull of the user')
parser.add_argument('email', type=str, required=True, help='the mail of the user')

class Send_pulls(Resource):
    def post(self):

        args = parser.parse_args(strict=True)
        new_card = Cardiaque(name=args['pulls'], rythme=args['pulls'], date=datetime.datetime.today().strftime('%Y-%m-%d'))

        db.session.add(new_card)
        db.session.commit()
        id_ = Cardiaque.query.filter_by(email=args['email']).first()
        return Response(
            response=id_.to_json(),
            status=200, mimetype='application/json')
