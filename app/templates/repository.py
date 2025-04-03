from bson import ObjectId
from app.core.entity_manager import EntityManager
from app.templates.models import Template

class TemplateRepository:
    collection_name = "templates"
    
    def __init__(self, entity_manager=None):
        self.entity_manager = entity_manager if entity_manager else EntityManager()
    
    def find(self, page, limit):
        templates_data, total_count = self.entity_manager.find(
            self.collection_name, 
            page=page, 
            limit=limit
        )
        
        templates = [Template.from_dict(template_data) for template_data in templates_data]
        
        return templates, total_count
        
    def persist(self, template):
        template_dict = template.to_dict()

        template_dict.pop("id", None)
        template_dict["_id"] = ObjectId(template.id)
        
        self.entity_manager.insert_one(self.collection_name, template_dict)
        return template
