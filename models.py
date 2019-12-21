from pymodm import MongoModel, fields

class User(MongoModel):
	first_name = fields.CharField(max_length = 50)
	last_name = fields.CharField(max_length = 50)
	email = fields.EmailField(primary_key = True)
	hashed_password = fields.CharField(max_length = 256)
	height_inches = fields.IntegerField(min_value = 0, max_value = 120)
	weight_lbs = fields.IntegerField(min_value = 0, max_value = 600)

class Workout(MongoModel):
	date = fields.DateTimeField()
	total_gym_time = fields.IntgerField(min_value = 0, max_value = 600)
	total_rest_time = fields.IntgerField(min_value = 0, max_value = 600)
	exercises = fields.EmbeddedDocumentListField('Exercise')

class Exercise(EmbeddedMongoModel):
	exercise_name = fields.CharField(max_lenght = 50)
	reps = fields.IntgerField(min_value = 0, max_value = 20)
	sets = fields.IntgerField(min_value = 0, max_value = 10)
	weight = fields.IntgerField(min_value = 0, max_value = 1000)
	time = fields.IntgerField(min_value = 0, max_value = 600)
