from flask_restful import reqparse, Resource
from flask import Response
import json
from src.models import Journeys

parser = reqparse.RequestParser()
parser.add_argument('email', type=str, required=True, help='mail of the user you want the information')


class getJourneys(Resource):
    def post(self):
        args = parser.parse_args(strict=True)
        journeys = Journeys.query.filter_by(email=args['email']).all()

        if journeys is None:
            return Response(
                response=json.dumps(dict(error='User doesn\'t exist')),
                status=400, mimetype='application/json')
        tmp = [{'id': elt.id, 'email': elt.email, 'time': elt.time, 'date': str(elt.date), 'sleepingTime': elt.sleepingTime, 'alarm': elt.alarm, 'destination': elt.destination} for elt in journeys]
        return Response(
            response=json.dumps(tmp),
            status=200, mimetype='application/json')
