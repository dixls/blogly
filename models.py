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
    img_url = db.Column(db.String(191))

class Post(db.Model):
    """Posts table"""

    __tablename__= "posts"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String)
    created_at = db.Column(db.DateTime, nullable=False, default=db.func.now())