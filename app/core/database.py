
from flask_pymongo import PyMongo
import sys

mongo = PyMongo()


class Database:
    @staticmethod
    def get_db():
        try:
            if not hasattr(mongo, 'db'):
                print("Warning: mongo.db not initialized yet.",
                      file=sys.stderr)
                return None

            print(f"Database successful!", file=sys.stderr)
            return mongo.db
        except Exception as e:
            print(f"Error accessing mongo.db: {str(e)}", file=sys.stderr)
            return None
