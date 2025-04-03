from bson import ObjectId
from app.core.database import mongo
import sys


class EntityManager:
    def __init__(self):
        pass

    def find_all(self, collection_name, query=None):
        if query is None:
            query = {}
        try:
            return list(mongo.db[collection_name].find(query))
        except Exception as e:
            print(f"Error in find_all: {str(e)}", file=sys.stderr)
            return []

    def find_one(self, collection_name, query):
        try:
            result = mongo.db[collection_name].find_one(query)
            return result
        except Exception as e:
            print(f"Error in find_one: {str(e)}", file=sys.stderr)
            return None

    def find_by_id(self, collection_name, id):
        try:
            result = mongo.db[collection_name].find_one({"_id": ObjectId(id)})
            return result
        except Exception as e:
            print(f"Error finding by ID: {str(e)}", file=sys.stderr)
            return None

    def find(self, collection_name, query=None, page=1, limit=10):
        if query is None:
            query = {}

        try:
            skip = (page - 1) * limit
            total_count = mongo.db[collection_name].count_documents(query)
            results = list(mongo.db[collection_name].find(query).skip(skip).limit(limit))
            return results, total_count
        except Exception as e:
            print(f"Error in find_paginated: {str(e)}", file=sys.stderr)
            return [], 0

    def insert_one(self, collection_name, document):
        try:
            result = mongo.db[collection_name].insert_one(document)
            return result.inserted_id
        except Exception as e:
            print(f"Error in insert_one: {str(e)}", file=sys.stderr)
            return None