from flask import Flask
from flask import jsonify
from flask import request
from flask_pymongo import PyMongo

mongo = PyMongo()


def create_app():
	app = Flask(__name__)

	app.config['MONGO_DBNAME'] = 'test'
	app.config['MONGO_URI'] = 'mongodb+srv://Darien:test123@fitnesssystem-wtaxp.mongodb.net/test?retryWrites=true&w=majority'

	mongo.init_app(app)

	from .auth import auth as auth_blueprint
	app.register_blueprint(auth_blueprint)

	from .test_routes import test_routes as test_routes_blueprint
	app.register_blueprint(test_routes_blueprint)

	return app
