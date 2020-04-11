from flask import Flask
from flask_restful import Api
from application.config import DevelopmentConfig
from application.database import Database

app = Flask(__name__, static_url_path='/static')
api = Api(app)
app.config.from_object(DevelopmentConfig)
db = Database(app)

import application.handlers
