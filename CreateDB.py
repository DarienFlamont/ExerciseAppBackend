import pymongo

client = pymongo.MongoClient("mongodb+srv://Darien:test123@fitnesssystem-wtaxp.mongodb.net/test?retryWrites=true&w=majority")
db = client.test

print(client.list_database_names())
