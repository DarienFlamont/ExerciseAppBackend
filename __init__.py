from flask import Flask
from flask_pymongo import PyMongo
from flask_login import LoginManager

mongo = PyMongo()


def create_app():
	app = Flask(__name__)

	app.config['MONGO_DBNAME'] = 'test'
	app.config['MONGO_URI'] = 'mongodb+srv://Darien:test123@fitnesssystem-wtaxp.mongodb.net/test?retryWrites=true&w=majority'

	mongo.init_app(app)

	login_manager = LoginManager()
	login_manager.login_view = 'auth.login'
	login_manager.init_app(app)

	from .models import User

	@login_manager.user_loader
	def load_user(user_id):
		return mongo.db.users.find({'user_id': user_id})

	from .auth import auth as auth_blueprint
	app.register_blueprint(auth_blueprint)

	from .test_routes import test_routes as test_routes_blueprint
	app.register_blueprint(test_routes_blueprint)

	return app
