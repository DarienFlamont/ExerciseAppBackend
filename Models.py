from pymodm import MongoModel, fields

class User(MongoModel):
	first_name = fields.CharField(max_length = 50)
	last_name = fields.CharField(max_length = 50)
	email = fields.EmailField(primary_key = True)
	height_feet = fields.IntegerField(min_value = 0, max_length  = 10)
	height_inches = fields.IntegerField(min_value = 0, max_value = 13)
	weight_lbs = fields.IntegerField(min_value = 0, max_value = 600)