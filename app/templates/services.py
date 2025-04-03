from app.templates.repository import TemplateRepository

class TemplateService:
    def __init__(self, template_repository=None):
        self.template_repository = template_repository if template_repository else TemplateRepository()
    
    def get_all(self, page, limit):
        if page < 1:
            page = 1
        if limit < 1 or limit > 100:
            limit = 10
            
        return self.template_repository.find(page, limit)
        
    def persist(self, template):
        return self.template_repository.persist(template)
