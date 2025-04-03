from datetime import datetime
from bson import ObjectId
from app.core.base_model import BaseModel

class Template(BaseModel):
    
    def __init__(self, title=None, description=None, created_at=None, id=None, created_by=None):
        super().__init__(id=id, created_at=created_at)
        self.title = title
        self.description = description
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
            "title": self.title,
            "description": self.description,
            "created_at": self.created_at,
            "created_by": self.created_by,
        }
