import pymongo

#Creating the client from our Atlas MongoDB
client = pymongo.MongoClient("mongodb+srv://Darien:test123@fitnesssystem-wtaxp.mongodb.net/test?retryWrites=true&w=majority")
db = client.test

workouts_collection = db['workouts']
users_collection = db['users']
exercise_hierarchy_collection = db['exercise_hierarchy']

#prints all the collections in the DB
print(db.list_collection_names())
