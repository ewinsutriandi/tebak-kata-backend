from flask_restful import Resource
from flask import request
from application import app, db, api

@api.route('/health')
class Test(Resource):
    #method_decorators=[wrap_test]
    def get(self):
        return {
			'database':'connected = {}'.format(db_test())
		}

def db_test():
	try:
		conn = db.getconn()
		if conn:
			return True
	except Exception as e:
		print(e)
	return False
    