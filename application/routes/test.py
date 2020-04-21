from flask_restful import Resource
from flask import request
from application import app, db, api

@api.route('/health')
class Test(Resource):
		#method_decorators=[wrap_test]		
		def get(self):
			connected = db_test()
			test_result = {}
			if connected:
				test_result['db'] = 'DB is connected' 
				time = db_time()
				test_result['server time'] = str(time)
			else:
				test_result['db'] = 'DB is not connected' 
			return test_result

def db_test():
	try:
		conn = db.getconn()
		if conn:
			return True
	except Exception as e:
		print(e)
	return False

def db_time():
	try:
		conn = db.getconn()
		return db.get_single_val_query('select now()')
	except Exception as e:
		print(e)
	return False
