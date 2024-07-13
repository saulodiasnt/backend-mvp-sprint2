from pydantic import BaseModel, Field
from typing import Optional


class CreateUserFavoriteSchema(BaseModel):
    title: str = Field(None, examples="The Godfather")
    backdrop_path: Optional[str] = Field(None, examples="/path")
    poster_path: Optional[str] = Field(None, examples="/path")
    media_type: Optional[str] = Field(None, examples="movie")
    tmdb_id: int = Field(None, examples=1)

    
    
