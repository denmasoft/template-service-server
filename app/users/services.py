from app.users.repository import UserRepository
from app.core.entity_manager import EntityManager


class UserService:
    def __init__(self, user_repository=None):
        self.user_repository = user_repository if user_repository else UserRepository()

    def get_all(self, page, limit):
        if page < 1:
            page = 1
        if limit < 1 or limit > 100:
            limit = 10

        return self.user_repository.find(page, limit)

    def get_user_by_id(self, user_id):
        return self.user_repository.find_by_id(user_id)

    def get_user_by_google_id(self, google_id):
        return self.user_repository.find_by_google_id(google_id)

    def save_user(self, user):
        return self.user_repository.persist(user)
