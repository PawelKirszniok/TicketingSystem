from flask import Flask
from flask_restful import Resource, Api, abort
from db import DatabaseService
from Verification import verify_code


import jsonpickle

app = Flask(__name__)
api = Api(app)
ds = DatabaseService()


class GetUser(Resource):

    def post(self, raw_data):

        data = jsonpickle.decode(raw_data)

        # Validation
        if not verify_code(data['secretkey']):
            return abort(403, "Incorrect authorization, access denied")

        payload = data['payload']

        result = ds.get_user(payload['id'])
        return jsonpickle.encode(result)


class GetTickets(Resource):

    def post(self, raw_data):
        data = jsonpickle.decode(raw_data)

        # Validation
        if not verify_code(data['secretkey']):
            return abort(403, "Incorrect authorization, access denied")

        payload = data['payload']

        if 'role' in payload:
            result = ds.search_ticket(payload['user'], payload['role'])
        else:
            result = ds.search_ticket(payload['user'])
        return jsonpickle.encode(result)


class GetUsers(Resource):

    def post(self, raw_data):
        data = jsonpickle.decode(raw_data)

        # Validation
        if not verify_code(data['secretkey']):
            return abort(403, "Incorrect authorization, access denied")

        payload = data['payload']

        result = ds.search_user(payload['id'])
        return jsonpickle.encode(result)


class GetPosts(Resource):

    def post(self, raw_data):
        data = jsonpickle.decode(raw_data)

        # Validation
        if not verify_code(data['secretkey']):
            return abort(403, "Incorrect authorization, access denied")

        payload = data['payload']

        if 'ticket' in payload:
            result = ds.search_post(ticket=payload['ticket'])
        else:
            result = ds.search_post(user=payload['user'])
        return jsonpickle.encode(result)


class SaveUser(Resource):

    def post(self, raw_data):
        data = jsonpickle.decode(raw_data)

        # Validation
        if not verify_code(data['secretkey']):
            return abort(403, "Incorrect authorization, access denied")

        payload = data['payload']

        ds.save_user(payload['user'])
        return


class SaveTicket(Resource):

    def post(self, raw_data):
        data = jsonpickle.decode(raw_data)

        # Validation
        if not verify_code(data['secretkey']):
            return abort(403, "Incorrect authorization, access denied")

        payload = data['payload']

        ds.save_ticket(payload['ticket'])
        return


class SavePost(Resource):

    def post(self, raw_data):
        data = jsonpickle.decode(raw_data)

        # Validation
        if not verify_code(data['secretkey']):
            return abort(403, "Incorrect authorization, access denied")

        payload = data['payload']

        ds.save_post(payload['post'])
        return


class SaveRelationship(Resource):

    def post(self, raw_data):
        data = jsonpickle.decode(raw_data)

        # Validation
        if not verify_code(data['secretkey']):
            return abort(403, "Incorrect authorization, access denied")

        payload = data['payload']

        ds.save_relationship(payload['user'], payload['ticket'], payload['role'])
        return


api.add_resource(GetUser, '/getuser')
api.add_resource(GetUsers, '/getusers')
api.add_resource(GetTickets, '/gettickets')
api.add_resource(GetPosts, '/getposts')
api.add_resource(SaveUser, '/saveuser')
api.add_resource(SaveTicket, '/saveticket')
api.add_resource(SavePost, '/savepost')
api.add_resource(SaveRelationship, '/saverelation')


