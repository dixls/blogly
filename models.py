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

    def __repr__(self):
        return f"<USER name = {self.first_name} {self.last_name}, ID = {self.id}>"


class Post(db.Model):
    """Posts table"""

    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String)
    created_at = db.Column(db.DateTime, nullable=False, default=db.func.now())
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    author = db.relationship("User", backref="posts")

    tags = db.relationship("Tag", secondary="post_tags", backref="posts")

    def __repr__(self):
        return f"<post Title = {self.title}, AUTHOR = {self.author.first_name} {self.author.last_name}>"


class Tag(db.Model):
    """tags for a given post"""

    __tablename__ = "tags"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False, unique=True)


class PostTag(db.Model):
    """relationships of tags to posts"""

    __tablename__ = "posts_tags"

    tag_id = db.Column(db.Integer, db.ForeignKey("tags.id"), primary_key=True)
    post_id = db.Column(db.Integer, db.ForeignKey("posts.id"), primary_key=True)
