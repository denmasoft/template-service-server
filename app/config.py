import os
from datetime import timedelta
from dotenv import load_dotenv

load_dotenv()

class Config:
    MONGO_URI = os.getenv('MONGO_URI', '')

    DEBUG = os.getenv('DEBUG', 'False').lower() == 'true'
    APP_ENV = os.getenv('APP_ENV', 'dev')

    # CORS settings
    CORS_ORIGINS = os.getenv('CORS_ORIGINS', '*')
    CORS_METHODS = os.getenv('CORS_METHODS', 'GET,POST,PUT,DELETE,OPTIONS').split(',')
    CORS_ALLOW_HEADERS = os.getenv('CORS_ALLOW_HEADERS', 'Content-Type,Authorization').split(',')
    CORS_EXPOSE_HEADERS = os.getenv('CORS_EXPOSE_HEADERS', 'Content-Type,Authorization').split(',')
    CORS_SUPPORTS_CREDENTIALS = os.getenv('CORS_SUPPORTS_CREDENTIALS', 'True').lower() == 'true'

    # Rate limiting settings
    RATELIMIT_DEFAULT = os.getenv('RATELIMIT_DEFAULT', "")

    if RATELIMIT_DEFAULT.startswith('"') and RATELIMIT_DEFAULT.endswith('"'):
        RATELIMIT_DEFAULT = RATELIMIT_DEFAULT[1:-1]

    RATELIMIT_STRATEGY = os.getenv('RATELIMIT_STRATEGY', "fixed-window")
    RATELIMIT_STORAGE_URL = os.getenv('RATELIMIT_STORAGE_URL', "memory://")
    RATELIMIT_MINUTE = os.getenv('RATELIMIT_MINUTE')

    # JWT configuration
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', '')
    try:
        access_expires = int(os.getenv('JWT_ACCESS_TOKEN_EXPIRES', 3600))
    except (ValueError, TypeError):
        access_expires = 3600  # Default 1 hour

    try:
        refresh_expires = int(os.getenv('JWT_REFRESH_TOKEN_EXPIRES', 86400))
    except (ValueError, TypeError):
        refresh_expires = 86400  # Default 24 hours

    JWT_ACCESS_TOKEN_EXPIRES = timedelta(seconds=access_expires)
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(seconds=refresh_expires)