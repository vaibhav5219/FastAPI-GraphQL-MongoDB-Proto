from pymongo import MongoClient

MongoClient = MongoClient("mongodb://localhost:27017/")
db = MongoClient["sms"]
user_collection = db["users"]