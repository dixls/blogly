"""Models for Blogly."""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def connect_db(app):
    """connect to database"""
    db.app = app
    db.init_app(app)


class User(db.Model):
    """Users table"""

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(25), nullable=False)
    last_name = db.Column(db.String(40), nullable=False)
    image_url = db.Column(db.String(191))
