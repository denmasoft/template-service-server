import os
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
    RATELIMIT_DEFAULT = os.getenv('RATELIMIT_DEFAULT', "100 per day, 10 per hour")

    if RATELIMIT_DEFAULT.startswith('"') and RATELIMIT_DEFAULT.endswith('"'):
        RATELIMIT_DEFAULT = RATELIMIT_DEFAULT[1:-1]

    RATELIMIT_STRATEGY = os.getenv('RATELIMIT_STRATEGY', "fixed-window")
    RATELIMIT_STORAGE_URL = os.getenv('RATELIMIT_STORAGE_URL', "memory://")