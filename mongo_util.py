import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

# Get MongoDB URI and database name from .env file
MONGO_URI = os.getenv("MONGO_URI")
MONGO_DB_NAME = os.getenv("MONGO_DB_NAME")

# Initialize MongoDB connection
def init_mongo():
    mongo_client = MongoClient(MONGO_URI)
    db = mongo_client[MONGO_DB_NAME]
    user_collection = db['users']  # Collection to store user data
    return user_collection

# Update user state and name in MongoDB
def update_user_data(user_collection, phone_number, user_state, user_name):
    user_collection.update_one(
        {'phone_number': phone_number},
        {'$set': {'state': user_state, 'name': user_name}},
        upsert=True  # This will insert a new document if not exists
    )

# Retrieve user state and name from MongoDB
def get_user_data(user_collection, phone_number):
    user_data = user_collection.find_one({'phone_number': phone_number})
    if user_data:
        user_state = user_data.get('state', 'initial')
        user_name = user_data.get('name', '')
    else:
        user_state = 'initial'
        user_name = ''
    return user_state, user_name
