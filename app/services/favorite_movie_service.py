from app.models.favorite_movie import FavoriteMovie
from flask import jsonify
from app.database import db
from app.shared.erros import NotFoundException


class FavoriteMovieService:
    @staticmethod
    def get_all_user_favorite_movies(user_id: int):
        return FavoriteMovie.query.filter_by(user_id=user_id).all()

    @staticmethod
    def get_user_favorite_movie_by_id(task_id: int, user_id: int):
        return FavoriteMovie.query.filter_by(id=task_id, user_id=user_id).first()

    @staticmethod
    def create_user_favorite_movie(
        title: str,
        tmdb_id: int,
        backdrop_path: str,
        poster_path: str,
        user_id: int,
        media_type: str
    ):
        favorite_movie = FavoriteMovie(
            title=title,
            tmdb_id=tmdb_id,
            user_id=user_id,
            backdrop_path=backdrop_path,
            poster_path=poster_path,
            media_type=media_type

        )

        db.session.add(favorite_movie)
        db.session.commit()
        return favorite_movie

    @staticmethod
    def delete_user_favorite_movie(favorite_movie_id: int, user_id: int):
        favorite_movie = FavoriteMovie.query.filter_by(id=favorite_movie_id, user_id=user_id).first()
        if not favorite_movie:
            return NotFoundException().to_dict()
        db.session.delete(favorite_movie)
        db.session.commit()
        return jsonify(), 201
