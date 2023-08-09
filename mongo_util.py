import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
MONGO_DB_NAME = os.getenv("MONGO_DB_NAME")

def init_mongo():
    mongo_client = MongoClient(MONGO_URI)
    db = mongo_client[MONGO_DB_NAME]
    user_collection = db['users']
    return user_collection

def update_user_data(user_collection, phone_number, user_state, user_name):
    if user_state == 'initial':
        user_collection.delete_one({'phone_number': phone_number})
    else:
        user_collection.update_one(
            {'phone_number': phone_number},
            {'$set': {'state': user_state, 'name': user_name}},
            upsert=True
        )

def get_user_data(user_collection, phone_number):
    user_data = user_collection.find_one({'phone_number': phone_number})
    if user_data:
        user_state = user_data.get('state', 'initial')
        user_name = user_data.get('name', '')
    else:
        user_state = 'initial'
        user_name = ''
    return user_state, user_name
