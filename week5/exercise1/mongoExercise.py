#!C:/Users/Max/Anaconda/Python
import pymongo as pm
client = pm.MongoClient()

db = client.test_database

collection = db.test_collection

posts = db.posts

print posts.find_one()
