from datetime import datetime
from bson import ObjectId

class User:
    
    def __init__(self, google_id=None, name=None, email=None, picture=None, 
                 created_at=None, id=None):
        self.id = id if id else str(ObjectId())
        self.google_id = google_id
        self.name = name
        self.email = email
        self.picture = picture
        self.created_at = created_at if created_at else datetime.now()
    
    @classmethod
    def from_dict(cls, data):
        if not data:
            return None
            
        return cls(
            id=str(data.get('_id')) if data.get('_id') else None,
            google_id=data.get('google_id'),
            name=data.get('name'),
            email=data.get('email'),
            picture=data.get('picture'),
            created_at=data.get('created_at'),
        )
    
    def to_dict(self):
        return {
            "id": self.id,
            "google_id": self.google_id,
            "name": self.name,
            "email": self.email,
            "picture": self.picture,
            "created_at": self.created_at,
        }
