"""Blogly application."""

from flask import Flask, render_template, request, redirect
from models import db, connect_db, User, Post

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///blogly"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True

connect_db(app)
db.create_all()

from flask_debugtoolbar import DebugToolbarExtension

app.config["SECRET_KEY"] = "my_secret_key"
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False
debug = DebugToolbarExtension(app)


@app.route("/")
def root():
    """home page redirects to /users"""

    return redirect("/users/")


@app.route("/users/")
def user_list():
    """List of all current users."""

    users = User.query.all()
    return render_template("user-list.html", users=users)


@app.route("/users/new/")
def user_form():
    """displays form for creating a new user"""

    return render_template("user-form.html")


@app.route("/users/new/", methods=["POST"])
def add_user():
    """adds new user to users table"""

    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    img_url = request.form["img_url"]

    new_user = User(first_name=first_name, last_name=last_name, img_url=img_url)

    db.session.add(new_user)
    db.session.commit()

    return redirect(f"/users/{new_user.id}/")


@app.route("/users/<user_id>/")
def user_info(user_id):
    """shows info for a specific user"""

    user = User.query.get_or_404(user_id)
    return render_template("user-info.html", user=user)


@app.route("/users/<user_id>/edit/")
def user_edit(user_id):
    """shows info for a specific user"""

    user = User.query.get_or_404(user_id)
    return render_template("user-edit.html", user=user)


@app.route("/users/<user_id>/edit/", methods=["POST"])
def user_edit_submit(user_id):
    """shows info for a specific user"""

    updated_user = User.query.get(user_id)

    updated_user.first_name = request.form["first_name"]
    updated_user.last_name = request.form["last_name"]
    updated_user.img_url = request.form["img_url"]

    db.session.commit()

    return redirect(f"/users/{user_id}/")


@app.route("/users/<user_id>/delete/", methods=["POST"])
def user_delete(user_id):
    """delete user from database"""

    User.query.filter(User.id == user_id).delete()
    db.session.commit()

    return redirect("/users/")


@app.route("/tags/")
def list_tags():
    """list tags from database"""


@app.route("/tags/new/")
def new_tag_form():
    """display form for creating a new tag"""


@app.route("/tags/new/", methods=["POST"])
def submit_tag():
    """add new tag to db"""


@app.route("/tags/<tag_id>/")
def tag_info():
    """display informations about a tag"""


@app.route("/tags/<tag_id>/edit/")
def edit_tag():
    """displayu form for editting an existing tag"""


@app.route("/tags/<tag_id>/edit/", methods=["POST"])
def submit_edit_tag():
    """submit changes to a tag to the db"""


@app.route("/tags/<tag_id>/delete/", methods=["POST"])
def delete_tag():
    """delete a tag from the db"""