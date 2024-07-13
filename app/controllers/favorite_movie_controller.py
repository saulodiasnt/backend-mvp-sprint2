from flask import g
from flask_openapi3 import APIBlueprint, Tag
from app.services.favorite_movie_service import FavoriteMovieService
from app.schemas import (
CreateUserFavoriteSchema,
FavoriteMovieResponseSchema,
FavoriteMoviePathSchema
)
from app.shared.erros import NotFoundException, UnauthorizedException
from flask import jsonify

security = [{"jwt": []}]

favorite_movie_tag = Tag(name="Favorite Movies", description="")
favorite_movie_bp = APIBlueprint(
    "favorite-movies",
    __name__,
    url_prefix="/favorite-movies",
    abp_security=security,
    abp_tags=[favorite_movie_tag],
    abp_responses={404: NotFoundException, 401: UnauthorizedException},
)


@favorite_movie_bp.post("/", tags=[favorite_movie_tag], responses={201: FavoriteMovieResponseSchema})
def create_favorite_movie(body: CreateUserFavoriteSchema):
    user_id = g.get("current_user").id
    print(user_id)

    favorite_movie = FavoriteMovieService.create_user_favorite_movie(
        title=body.title,
        tmdb_id=body.tmdb_id,
        backdrop_path=body.backdrop_path,
        poster_path=body.poster_path,
        media_type=body.media_type,
        user_id=user_id,
    )

    return jsonify(favorite_movie.to_dict()), 201


@favorite_movie_bp.get("/", responses={200: FavoriteMovieResponseSchema})
def list_favorite_movie():
    user_id = g.get("current_user").id
    favorite_movies = FavoriteMovieService.get_all_user_favorite_movies(user_id)
    return jsonify([favorite_movie.to_dict() for favorite_movie in favorite_movies]), 200


@favorite_movie_bp.get("/<int:favorite_movie_id>", responses={200: FavoriteMovieResponseSchema})
def get_favorite_movie(path: FavoriteMoviePathSchema):
    user_id = g.get("current_user").id
    favorite_movie_id = path.favorite_movie_id

    favorite_movie = FavoriteMovieService.get_user_favorite_movie_by_id(favorite_movie_id, user_id)
    if not favorite_movie:
        return jsonify(error="Favorite Movie not found"), 404

    return jsonify(favorite_movie.to_dict()), 200


@favorite_movie_bp.delete("/<int:favorite_movie_id>", responses={204: None})
def delete_favorite_movie(path: FavoriteMoviePathSchema):
    user_id = g.get("current_user").id
    favorite_movie_id = int(path.favorite_movie_id)
    return FavoriteMovieService.delete_user_favorite_movie(favorite_movie_id, user_id)
