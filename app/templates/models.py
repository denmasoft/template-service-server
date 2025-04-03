from datetime import datetime
from bson import ObjectId

class Template:
    
    def __init__(self, title=None, description=None, created_at=None, id=None, created_by=None):
        self.id = id if id else str(ObjectId())
        self.title = title
        self.description = description
        self.created_at = created_at if created_at else datetime.now()
        self.created_by = created_by
    
    @classmethod
    def from_dict(cls, data):
        if not data:
            return None
            
        return cls(
            id=str(data.get('_id')) if data.get('_id') else None,
            title=data.get('title'),
            description=data.get('description'),
            created_at=data.get('created_at'),
            created_by=data.get('created_by'),
        )
    
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.title,
            "description": self.description,
            "created_at": self.created_at,
            "created_by": self.created_by,
        }
