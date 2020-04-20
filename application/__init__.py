import os
from flask import Flask
app = Flask(__name__, static_url_path='/static')

from flask_restful import Api
api = Api(app)

prod = os.getenv('PROD_MODE',default='false')
PROD_MODE = prod.lower() in (1,'t','true')
print('Production mode:',PROD_MODE) 
import application.config
if PROD_MODE:
	print('Load production configuration')   
	app.config.from_object(config.Production())
else:
	print('Load development configuration')
	app.config.from_object(config.Development())

from application.database import Database
db = Database(app)

import application.routes
