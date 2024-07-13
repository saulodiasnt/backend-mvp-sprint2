from flask_openapi3 import OpenAPI
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_cors import CORS

from app.database import db

from app.middlewares import middleware

from app.controllers.auth_controller import auth_bp
from app.controllers.favorite_movie_controller import favorite_movie_bp


jwt = {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"}

security_schemes = {"jwt": jwt}

app = OpenAPI(__name__, security_schemes=security_schemes)
app.config["OPENAPI_VERSION"] = "3.0.2"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite"
app.config["JWT_SECRET_KEY"]="super-secret"
CORS(app)
db.init_app(app)

migrate = Migrate(app, db)
jwt = JWTManager(app)

middleware.auth_check_middleware(app)

app.register_api(auth_bp)
app.register_api(favorite_movie_bp)

from app import models

