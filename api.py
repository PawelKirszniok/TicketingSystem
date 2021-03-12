from flask import Flask, request
from flask_restful import Resource, Api, abort
from db import DatabaseService
from Verification import verify_code
from Models.User import User
from Models.Ticket import Ticket
from Models.Post import Post
import json


app = Flask(__name__)
api = Api(app)
ds = DatabaseService()


class GetUser(Resource):

    def post(self):

        data = request.get_json(force=True, silent=True)

        # Validation
        if not verify_code(data['secretkey']):
            return abort(403, message="Incorrect authorization, access denied")

        payload = data['payload']

        result = ds.get_user(payload['id'])
        return result.to_json()


class GetTickets(Resource):

    def post(self):

        data = data = request.get_json(force=True, silent=True)

        # Validation
        if not verify_code(data['secretkey']):
            return abort(403, message="Incorrect authorization, access denied")

        payload = data['payload']

        if 'role' in payload:
            result = ds.search_ticket(payload['user'], payload['role'])
        else:
            result = ds.search_ticket(payload['user'])

        final = ""

        for ticket in result:

            final += ticket.to_json()
            final += ','

        final = final[:-1]
        return '[' + final + ']'


class GetUsers(Resource):

    def post(self):

        data = request.get_json(force=True, silent=True)

        # Validation
        if not verify_code(data['secretkey']):
            return abort(403, message="Incorrect authorization, access denied")

        payload = data['payload']

        result = ds.search_user(payload['id'])
        final = ""

        for user in result:
            final += user.to_json()
            final += ','

        final = final[:-1]
        return '[' + final + ']'


class GetPosts(Resource):

    def post(self):

        data = data = request.get_json(force=True, silent=True)

        # Validation
        if not verify_code(data['secretkey']):
            return abort(403, message="Incorrect authorization, access denied")

        payload = data['payload']

        if 'ticket' in payload:
            result = ds.search_post(ticket=payload['ticket'])
        else:
            result = ds.search_post(user=payload['user'])

        final = ""

        for item in result:
            final += item.to_json()
            final += ','

        final = final[:-1]
        return '[' + final + ']'


class SaveUser(Resource):

    def post(self):

        raw_data = request.get_json(force=True, silent=True)

        # Validation
        if not verify_code(raw_data['secretkey']):
            return abort(403, message="Incorrect authorization, access denied")

        payload = raw_data['payload']
        user = User.from_json(payload)

        ds.save_user(user)
        return


class SaveTicket(Resource):

    def post(self, raw_data):

        data = request.get_json(force=True, silent=True)

        # Validation
        if not verify_code(data['secretkey']):
            return abort(403, message="Incorrect authorization, access denied")

        payload = data['payload']
        ticket = Ticket.from_json(payload)

        ds.save_ticket(ticket)
        return


class SavePost(Resource):

    def post(self):

        data = request.get_json(force=True, silent=True)

        # Validation
        if not verify_code(data['secretkey']):
            return abort(403, message="Incorrect authorization, access denied")

        payload = data['payload']
        post = Post.from_json(payload)

        ds.save_post(post)
        return


class SaveRelationship(Resource):

    def post(self):

        data = request.get_json(force=True, silent=True)

        # Validation
        if not verify_code(data['secretkey']):
            return abort(403, message="Incorrect authorization, access denied")

        payload = data['payload']

        ds.save_relationship(payload['user'], payload['ticket'], payload['role'])
        return


class ValidateUser(Resource):

    def post(self):

        data = request.get_json(force=True, silent=True)

        # Validation
        if not verify_code(data['secretkey']):
            return abort(403, message="Incorrect authorization, access denied")

        payload = data['payload']

        if 'email' not in payload:
            user_id, valid_password = ds.validate_user(payload['password'], login=payload['login'])
            result = {'user_id': user_id, 'valid_password': valid_password}
            return json.dumps(result)

        elif 'login' not in payload:
            user_id, valid_password = ds.validate_user(payload['password'], email=payload['email'])
            result = {'user_id': user_id, 'valid_password': valid_password}
            return json.dumps(result)

        else:
            user_id, valid_password = ds.validate_user(payload['password'], login=payload['login'], email=payload['email'])
            result = {'user_id': user_id, 'valid_password': valid_password}
            return json.dumps(result)


class StrSearchUsers(Resource):

    def post(self):

        data = request.get_json(force=True, silent=True)

        # Validation
        if not verify_code(data['secretkey']):
            return abort(403, message="Incorrect authorization, access denied")

        payload = data['payload']

        result = ds.str_search_user(payload['text'])
        final = ""

        for user in result:
            final += user.to_json()
            final += ','

        final = final[:-1]
        return '[' + final + ']'


api.add_resource(GetUser, '/getuser')
api.add_resource(GetUsers, '/getusers')
api.add_resource(GetTickets, '/gettickets')
api.add_resource(GetPosts, '/getposts')
api.add_resource(SaveUser, '/saveuser')
api.add_resource(SaveTicket, '/saveticket')
api.add_resource(SavePost, '/savepost')
api.add_resource(SaveRelationship, '/saverelation')
api.add_resource(ValidateUser, '/validateuser')
api.add_resource(StrSearchUsers, '/strsearchusers')


