from pymodm import MongoModel, EmbeddedMongoModel, fields, connect
from flask_login import UserMixin

connect('mongodb+srv://Darien:test123@fitnesssystem-wtaxp.mongodb.net/test?retryWrites=true&w=majority')


class User(UserMixin, MongoModel):
	id = fields.IntegerField(min_value=0, primary_key=True)
	first_name = fields.CharField(max_length=50)
	last_name = fields.CharField(max_length=50)
	email = fields.EmailField()
	hashed_password = fields.CharField(max_length=256)
	height_inches = fields.IntegerField(min_value=0, max_value=120)
	weight_lbs = fields.IntegerField(min_value=0, max_value=600)


class Workout(MongoModel):
	date = fields.DateTimeField()
	total_gym_time = fields.IntegerField(min_value=0, max_value=600)
	total_rest_time = fields.IntegerField(min_value=0, max_value=600)
	exercises_completed = fields.EmbeddedDocumentListField('CompletedExercise')


class CompletedExercise(EmbeddedMongoModel):
	exercise_name = fields.CharField(max_length=50, primary_key=True)
	exercise_classification = fields.CharField(max_length=50)
	reps = fields.IntegerField(min_value=0, max_value=20)
	sets = fields.IntegerField(min_value=0, max_value=10)
	weight = fields.IntegerField(min_value=0, max_value=1000)
	time = fields.IntegerField(min_value=0, max_value=600)
