#!C:/Users/Max/Anaconda/Python
import pymongo as pm
client = pm.MongoClient()
db = client.Northwind

collection = db.regions


print "inserting object"
result = collection.insert_one({'x':1})

print "successfully added object"
print collection.inserted_id

print "searching for object"
print collection.find({'x':1})

print "deleting object"
result = collection.delete_one({'x':1})
print "successfully deleted object"

#Look for object after deletion
print collection.find_one({'x':1})