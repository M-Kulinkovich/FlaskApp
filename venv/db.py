from flask import Flask
import pymongo
from pymongo import MongoClient
from __init__ import app

CONNECTION_STRING = "mongodb+srv://name:pass@namedb.mz0orda.mongodb.net/?retryWrites=true&w=majority"
client = pymongo.MongoClient(CONNECTION_STRING)
db = client.get_database('testdata')
user_collection = pymongo.collection.Collection(db, 'user_collection')
