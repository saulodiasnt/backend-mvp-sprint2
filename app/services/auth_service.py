from flask import jsonify
from datetime import timedelta
from flask_jwt_extended import create_access_token
from app.models.user import User
from app.database import db
from app.shared.erros import UnauthorizedException


class AuthService:
    @staticmethod
    def login(email: str, password: str):

        user = User.query.filter_by(email=email).first()

        if user is None or not user.check_password(password):
            return UnauthorizedException("Invalid email or password.").to_dict()
        expire_delta = timedelta(days=1)
        access_token = create_access_token(identity=user.id, expires_delta=expire_delta)

        return jsonify(access_token=access_token, user=user.to_dict())

    @staticmethod
    def register(name: str, email: str, password: str):
        user = User(name=name, email=email)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        return jsonify(user.to_dict())
