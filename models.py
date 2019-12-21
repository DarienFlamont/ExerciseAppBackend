from pymodm import MongoModel, fields

class User(MongoModel):
	first_name = fields.CharField(max_length = 50)
	last_name = fields.CharField(max_length = 50)
	email = fields.EmailField(primary_key = True)
	hashed_password = fields.CharField(max_length = 256)
	height_inches = fields.IntegerField(min_value = 0, max_value = 120)
	weight_lbs = fields.IntegerField(min_value = 0, max_value = 600)