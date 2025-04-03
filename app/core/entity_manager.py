from bson import ObjectId
from app.core.database import Database
import sys


class EntityManager:
    def __init__(self):
        self.db = Database.get_db()

    def find_all(self, collection_name, query=None):
        if query is None:
            query = {}
        try:
            return list(self.db[collection_name].find(query))
        except Exception as e:
            print(f"Error in find_all: {str(e)}", file=sys.stderr)
            return []

    def find_one(self, collection_name, query):
        try:
            result = self.db[collection_name].find_one(query)
            return result
        except Exception as e:
            print(f"Error in find_one: {str(e)}", file=sys.stderr)
            return None

    def find_by_id(self, collection_name, id):
        try:
            result = self.db[collection_name].find_one({"_id": ObjectId(id)})
            return result
        except Exception as e:
            print(f"Error finding by ID: {str(e)}", file=sys.stderr)
            return None

    def find(self, collection_name, query=None, page=1, limit=10):
        if query is None:
            query = {}

        try:
            skip = (page - 1) * limit
            total_count = self.db[collection_name].count_documents(query)
            results = list(self.db[collection_name].find(query).skip(skip).limit(limit))
            return results, total_count
        except Exception as e:
            print(f"Error in find_paginated: {str(e)}", file=sys.stderr)
            return [], 0

    def insert_one(self, collection_name, document):
        try:
            result = self.db[collection_name].insert_one(document)
            return result.inserted_id
        except Exception as e:
            print(f"Error in insert_one: {str(e)}", file=sys.stderr)
            return None