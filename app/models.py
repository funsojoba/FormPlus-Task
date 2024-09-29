import os
from app import mongo
from pymongo import MongoClient
from bson.objectid import ObjectId
from config import Config

client = MongoClient(Config.MONGO_URI)
db = client[os.environ.get('MONGODB_DATABASE')]
responses_collection = db['responses']

def create_form(data):
    form = {
        "title": data.get("title"),
        "description": data.get("description"),
        "fields": data.get("fields"),  # List of fields with type, label, etc.
        "created_by": data.get("created_by"),
        "created_at": data.get("created_at"),
    }
    return mongo.db.forms.insert_one(form)

def get_form(form_id):
    return mongo.db.forms.find_one({"_id": form_id})

def update_form(form_id, data):
    return mongo.db.forms.update_one({"_id": form_id}, {"$set": data})

def delete_form(form_id):
    return mongo.db.forms.delete_one({"_id": form_id})


def create_response(form_id, response_data):
    """
    Save a response to the given form.

    :param form_id: The ID of the form to which the response belongs.
    :param response_data: The actual response data submitted by the user.
    :return: The ID of the inserted response document.
    """
    response = {
        "form_id": ObjectId(form_id),
        "response_data": response_data,
        "submitted_at": datetime.utcnow()
    }
    result = responses_collection.insert_one(response)
    return result.inserted_id
