from bson import ObjectId
import time


class BaseModel:
    def __init__(self, id=None, created_at=None):
        self.id = id if id else str(ObjectId())
        self.created_at = created_at if created_at is not None else int(time.time())

    @classmethod
    def from_dict(cls, data):
        if not data:
            return None

        raise NotImplementedError("Child classes must implement from_dict")

    def to_dict(self):
        raise NotImplementedError("Child classes must implement to_dict")
