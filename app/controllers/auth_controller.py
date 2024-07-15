from app.services.auth_service import AuthService
from app.schemas.login_schema import LoginSchema
from app.schemas.register_schema import RegisterSchema
from flask import jsonify
from flask_openapi3 import Tag, APIBlueprint
from flask_cors import CORS

auth_tag = Tag(name="Auth", description="Endpoints for user authentication.")
auth_bp = APIBlueprint("auth", __name__, abp_tags=[auth_tag])

CORS(auth_bp)


@auth_bp.post(
    "/login",
    summary="Authenticates a user by checking the provided email and password.",
    description="Authenticates a user by checking the provided email and password.",
    tags=[auth_tag],
)
def login(body: LoginSchema):
    return AuthService.login(body.email, body.password)


@auth_bp.post(
    "/register",
    summary="Register a new user.",
    description="Register a new user.",
    tags=[auth_tag],
)
def register(body: RegisterSchema):
    try:
        return AuthService.register(body.name, body.email, body.password)
    except Exception as e:
        return jsonify(error=str(e)), 401
