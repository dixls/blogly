"""Blogly application."""

from flask import Flask, render_template, request, redirect
from models import db, connect_db, User

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///blogly"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True

connect_db(app)
db.create_all()

from flask_debugtoolbar import DebugToolbarExtension
app.config['SECRET_KEY'] = "my_secret_key"
debug = DebugToolbarExtension(app)

@app.route("/")
def root():
    """home page redirects to /users"""

    return redirect("/users")


@app.route("/users")
def user_list():
    """List of all current users."""

    users = User.query.all()
    return render_template("user-list.html", users=users)
