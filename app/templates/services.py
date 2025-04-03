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

    def get_by_title(self, title):
        return self.template_repository.find_by_title(title)

    def validate_unique_template(self, template):
        """
        Validate that the template title is unique
        """
        if not template or not template.title:
            return False, "Template name is required"

        existing_template = self.get_by_title(template.title)

        if existing_template and (not template.id or existing_template.id != template.id):
            return False, f"Template with title '{template.title}' already exists"

        return True, None
        
    def persist(self, template):
        is_valid, error_message = self.validate_unique_template(template)
        if not is_valid:
            raise ValueError(error_message)

        return self.template_repository.persist(template)
