import pymongo

#Creating the client from our Atlas MongoDB
client = pymongo.MongoClient("mongodb+srv://Darien:test123@fitnesssystem-wtaxp.mongodb.net/test?retryWrites=true&w=majority")

#test is the database on the cluster that we are inserting collections into (can also be done on Atlas interface)
db = client.test

workouts_collection = db['workouts']
users_collection = db['users']
exercise_hierarchy_collection = db['exercise_hierarchy']

#prints all the collections in the DB
print(db.list_collection_names())

#Try inserting a user
#user = {'name': 'Darien', 'weight': '160lbs', 'height': '6\'0'}

#Insert_one returns a object that has a property inserted_id that is some kind of hash (running this script will insert multiple Darien's)
#x = users_collection.insert_one(user)
#print(x.inserted_id)

