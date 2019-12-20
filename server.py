from flask import Flask
from flask import jsonify
from flask import request
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'test'
app.config['MONGO_URI'] = 'mongodb+srv://Darien:test123@fitnesssystem-wtaxp.mongodb.net/test?retryWrites=true&w=majority'

mongo = PyMongo(app)


@app.route('/user', methods=['GET'])
def get_all_users():
	users = mongo.db.users
	output = []
	for u in users.find():
		output.append({'name' : u['name'], 'weight' : u['weight'], 'height' : u['height']})
	return jsonify({'result': output})


if __name__ == '__main__':
	app.run(debug=True)