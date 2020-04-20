import types
from flask_restful import Resource
from flask import request
from application import app, db, api

# enable routing via decorators with Flask-RESTful
def api_route(self, *args, **kwargs):
    def wrapper(cls):
        self.add_resource(cls, *args, **kwargs)
        return cls
    return wrapper

api.route = types.MethodType(api_route, api)

# root route
@api.route('/')
class Hello(Resource):
    #method_decorators=[wrap_test]
    def get(self):
        return {'message':'Tebak kata backend API'}

import application.routes.test