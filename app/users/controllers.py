from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity, create_access_token, create_refresh_token

from app.config import Config
from app.users.services import UserService
from app.core.limiter import limiter
from app.api.response import ApiResponse
from app.users.models import User

users_bp = Blueprint('users', __name__)
user_service = UserService()

@users_bp.route('/', methods=['GET'])
@limiter.limit(Config.RATELIMIT_MINUTE)
@jwt_required()
def get_users():
    """
    Get all users
    """
    try:
        page = int(request.args.get('page', 1))
        limit = int(request.args.get('limit', 10))
        users, total_count = user_service.get_all(page, limit)

        users_dict = [user.to_dict() for user in users]

        pagination = {
            "count": total_count,
            "page": page
        }

        return ApiResponse.success(users_dict, pagination)
    except Exception as e:
        return ApiResponse.error(str(e), 500)

@users_bp.route('/google', methods=['POST'])
@limiter.limit(Config.RATELIMIT_MINUTE)
def register_google_user():
    try:
        data = request.get_json()

        if not data or not data.get('google_id') or not data.get('email'):
            return ApiResponse.error("Invalid request", 400)

        user = user_service.get_user_by_google_id(data.get('google_id'))

        if not user:
            user = User(
                google_id=data.get('google_id'),
                email=data.get('email'),
                name=data.get('name'),
                picture=data.get('picture'),
            )

            user_service.save_user(user)

        access_token = create_access_token(identity=user.id)
        refresh_token = create_refresh_token(identity=user.id)

        response_data = {
            "access_token": access_token,
            "refresh_token": refresh_token,
        }

        return ApiResponse.success(response_data)

    except Exception as e:
        return ApiResponse.error(str(e), 500)
