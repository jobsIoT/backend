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
        tmp = [{'id': elt.id, 'email': elt.email, 'rythme': elt.rythme, 'date': elt.date} for elt in pulls]
        return Response(
            response=json.dumps(tmp),
            status=200, mimetype='application/json')
