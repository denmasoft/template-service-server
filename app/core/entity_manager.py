from bson import ObjectId
from app.core.database import Database


class EntityManager:
    def __init__(self):
        self.db = Database.get_db()

    def find_all(self, collection_name, query=None):
        if query is None:
            query = {}
        return list(self.db[collection_name].find(query))

    def find_one(self, collection_name, query):
        return self.db[collection_name].find_one(query)

    def find_by_id(self, collection_name, id):
        try:
            return self.db[collection_name].find_one({"_id": ObjectId(id)})
        except:
            return None

    def find_paginated(self, collection_name, query=None, page=1, limit=10):
        if query is None:
            query = {}

        skip = (page - 1) * limit
        total_count = self.db[collection_name].count_documents(query)
        results = list(self.db[collection_name].find(query).skip(skip).limit(limit))

        return results, total_count

    def insert_one(self, collection_name, document):
        result = self.db[collection_name].insert_one(document)
        return result.inserted_id

    def update_one(self, collection_name, query, update_data):
        result = self.db[collection_name].update_one(
            query,
            {"$set": update_data}
        )
        return result.modified_count

    def delete_one(self, collection_name, query):
        result = self.db[collection_name].delete_one(query)
        return result.deleted_count