from pydantic import BaseModel, Field


class FavoriteMoviePathSchema(BaseModel):
    favorite_movie_id: int = Field(
        int, alias="favorite_movie_id", description="Favorite Movie ID", example=1
    )
