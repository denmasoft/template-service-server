from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity

from app.config import Config
from app.templates.services import TemplateService
from app.templates.models import Template
from app.users.services import UserService
from app.core.limiter import limiter
from app.api.response import ApiResponse

templates_bp = Blueprint('templates', __name__)
template_service = TemplateService()
user_service = UserService()

@templates_bp.route('/', methods=['GET'])
@limiter.limit(Config.RATELIMIT_MINUTE)
@jwt_required()
def get_templates():
    """
    Get all templates
    """
    try:
        page = int(request.args.get('page', 1))
        limit = int(request.args.get('limit', 10))
        templates, total_count = template_service.get_all(page, limit)

        templates_dict = [template.to_dict() for template in templates]
        
        pagination = {
            "count": total_count,
            "page": page,
            "limit": limit
        }
        
        return ApiResponse.success(templates_dict, pagination)
    except Exception as e:
        return ApiResponse.error(str(e), 500)

@templates_bp.route('/', methods=['POST'])
@limiter.limit(Config.RATELIMIT_MINUTE)
@jwt_required()
def create_template():
    try:
        data = request.get_json()
        
        if not data or not data.get('title') or not data.get('description'):
            return ApiResponse.error("title and description are required", 400)

        user_id = get_jwt_identity()
        user = user_service.get_user_by_id(user_id)
        
        if not user:
            return ApiResponse.error("User not found", 404)

        template = Template(
            title=data.get('title'),
            description=data.get('description'),
            created_by=user.email
        )

        try:
            saved_template = template_service.persist(template)
            return ApiResponse.success(saved_template.to_dict())
        except ValueError as ve:
            return ApiResponse.error(str(ve), 400)

    except Exception as e:
        return ApiResponse.error(str(e), 500)

