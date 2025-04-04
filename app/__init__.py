from flask import Flask
from app.config import Config
from app.core.database import mongo
from flask_cors import CORS
from app.core.limiter import limiter
from flask_jwt_extended import JWTManager
from app.users.controllers import users_bp
from app.templates.controllers import templates_bp

def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)
    jwt = JWTManager(app)
    limiter.init_app(app)
    mongo.init_app(app)
    app.url_map.strict_slashes = False

    # Configure CORS
    origins = Config.CORS_ORIGINS.split(',') if isinstance(Config.CORS_ORIGINS,
                                                           str) and ',' in Config.CORS_ORIGINS else Config.CORS_ORIGINS
    CORS(app,
         resources={r"/*": {"origins": origins}},
         methods=Config.CORS_METHODS,
         allow_headers=Config.CORS_ALLOW_HEADERS,
         expose_headers=Config.CORS_EXPOSE_HEADERS,
         supports_credentials=Config.CORS_SUPPORTS_CREDENTIALS)

    app.register_blueprint(users_bp, url_prefix='/users')
    app.register_blueprint(templates_bp, url_prefix='/templates')

    return app
