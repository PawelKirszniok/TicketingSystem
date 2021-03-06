from flask import Flask
from flask_restful import Resource, Api, abort
from db import DatabaseService
from configparser import ConfigParser

import jsonpickle

app = Flask(__name__)
api = Api(app)
ds = DatabaseService()


class ApiHandler(Resource):

    def post(self, raw_data):
        config_object = ConfigParser()
        config_object.read("config.ini")

        keys = config_object['KEYS']
        data = jsonpickle.decode(raw_data)

        # Validation
        if data['secretkey'] != keys['secretkey']:
            return abort(403, "Incorrect authorization, access denied")

        mode = data['mode']
        payload = data['payload']

        # Case Handling
        if mode == 'get_user':
            result = ds.get_user(payload['id'])
            return jsonpickle.encode(result)

        if mode == 'get_tickets':
            if 'role' in payload:
                result = ds.search_ticket(payload['user'], payload['role'])
            else:
                result = ds.search_ticket(payload['user'])
            return jsonpickle.encode(result)

        if mode == 'get_users':
            result = ds.search_user(payload['id'])
            return jsonpickle.encode(result)

        if mode == 'get_posts':
            if 'ticket' in payload:
                result = ds.search_post(ticket=payload['ticket'])
            else:
                result = ds.search_post(user=payload['user'])
            return jsonpickle.encode(result)

        if mode == 'save_user':
            ds.save_user(payload['user'])
            return

        if mode == 'save_ticket':
            ds.save_ticket(payload['ticket'])
            return

        if mode == 'save_post':
            ds.save_post(payload['post'])
            return

        if mode == 'save_relation':
            ds.save_relationship(payload['user'], payload['ticket'], payload['role'])
            return


api.add_resource(ApiHandler, '/')
