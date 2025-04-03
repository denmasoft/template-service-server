from bson import ObjectId
from app.core.entity_manager import EntityManager
from app.users.models import User


class UserRepository:
    collection_name = "users"

    def __init__(self, entity_manager=None):
        self.entity_manager = entity_manager if entity_manager else EntityManager()

    def find(self, page, limit):
        users_data, total_count = self.entity_manager.find(
            self.collection_name,
            page=page,
            limit=limit
        )

        users = [User.from_dict(user_data) for user_data in users_data]

        return users, total_count

    def find_by_google_id(self, google_id):
        print(f"{google_id}")
        user_data = self.entity_manager.find_one(self.collection_name, {"google_id": google_id})
        print(f"{user_data}")
        if user_data is None:
            return None
        return User.from_dict(user_data)

    def persist(self, user):
        user_dict = user.to_dict()

        user_dict.pop("id", None)
        user_dict["_id"] = ObjectId(user.id)

        self.entity_manager.insert_one(self.collection_name, user_dict)
        return user
