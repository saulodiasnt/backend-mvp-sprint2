from app.database import db

import datetime

class FavoriteMovie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    tmdb_id = db.Column(db.Integer, nullable=False)
    backdrop_path = db.Column(db.String(255), nullable=False)
    poster_path = db.Column(db.String(255), nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    media_type = db.Column(db.String(80), nullable=True, default='movie')
    created_at = db.Column(db.DateTime, default=datetime.datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now)

    def __repr__(self):
        return f"<FavoriteMovie {self.title}>"

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "tmdb_id": self.tmdb_id,
            "backdrop_path": self.backdrop_path,
            "poster_path": self.poster_path,
            "user_id": self.user_id,
            "media_type": self.media_type,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }