import json
from flask_restful import Resource
from flask import Response
from src.models import User


class getUsers(Resource):
    def post(self):
        id_ = User.query.all()
        tmp = [{'email': elt.email, 'firstname': elt.firstname, 'lastname': elt.lastname, 'password': elt.password, 'ispremium': elt.ispremium, 'serialnumber': elt.serialnumber, 'isadmin': elt.isadmin} for elt in id_]
        if id_ is None:
            return Response(
                response=json.dumps(dict(error='User doesn\'t exist')),
                status=400, mimetype='application/json')
        return Response(
                response=json.dumps(tmp),
                status=200, mimetype='application/json')
