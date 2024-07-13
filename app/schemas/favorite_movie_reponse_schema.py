from pydantic import BaseModel, Field


class FavoriteMovieResponseSchema(BaseModel):
    id: int = Field(..., description="The unique identifier for the task")
    title: str = Field(..., description="The title of the movie")
    backdrop_path: str = Field(..., description="The backdrop path of the movie")
    tmdb_id: int = Field(..., description="The tmdb id of the movie")
    user_id: int = Field(..., description="The user id of the movie")
    created_at: str = Field(..., description="The date the movie was created")
    updated_at: str = Field(..., description="The date the movie was updated")
