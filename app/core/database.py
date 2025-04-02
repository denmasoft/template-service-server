from flask_pymongo import PyMongo

mongo = PyMongo()

class Database:
    @staticmethod
    def get_db():
        return mongo.db
