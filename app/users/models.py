from datetime import datetime
from bson import ObjectId
from app.core.base_model import BaseModel

class User(BaseModel):
    
    def __init__(self, google_id=None, name=None, email=None, picture=None, 
                 created_at=None, id=None):
        super().__init__(id=id, created_at=created_at)
        self.google_id = google_id
        self.name = name
        self.email = email
        self.picture = picture
    
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
