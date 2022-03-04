from hashlib import new
from http.client import FOUND
from unittest import TestCase
from http import HTTPStatus

from app import app
from models import db, User

# Use test database and don't clutter tests with SQL
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///blogly_test"
app.config["SQLALCHEMY_ECHO"] = False

# Make Flask errors be real errors, rather than HTML pages with error info
app.config["TESTING"] = True

# This is a bit of hack, but don't use Flask DebugToolbar
app.config["DEBUG_TB_HOSTS"] = ["dont-show-debug-toolbar"]

db.drop_all()
db.create_all()


class RouteTest(TestCase):
    """test route responses"""

    def setUp(self) -> None:

        new_user = User(
            first_name="Jack",
            last_name="Sparrow",
            img_url="https://i1.sndcdn.com/artworks-1kK2LeUMqtUH5SIx-IIYPDA-t500x500.jpg",
        )
        db.session.add(new_user)
        db.session.commit()

    def tearDown(self) -> None:

        db.session.rollback()
        User.query.delete()
        db.session.commit()

    def test_root(self):
        with app.test_client() as client:
            resp = client.get("/")

            self.assertTrue(HTTPStatus.FOUND)

    def test_users(self):
        with app.test_client() as client:
            resp = client.get("/users/")
            html = resp.get_data(as_text=True)

            self.assertTrue(HTTPStatus.OK)
            self.assertIn("Jack Sparrow", html)
