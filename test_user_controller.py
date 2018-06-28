from unittest import TestCase
from app import db, app, connect_to_db
from models import User, example_data

connect_to_db(app, db_uri="postgres://localhost/warbler_db_test")


class UserControllerTests(TestCase):
    def setUp(self):
        db.create_all()
        example_data()

    def tearDown(self):
        db.session.close()
        db.drop_all()

    # Test that a user who isn't logged in cannot access routes
    # requiring a login
    def test_authenticated_routes(self):
        client = app.test_client()
        response = client.get('/users/1/following', follow_redirects=True)
        # self.assertIn(b'Welcome back.', response.data)

    # Test user creation process (i.e. after form is submitted,
    # a user's info is properly displayed on profile page)
    def test_user_creation_routes(self):
        pass

    # Test user editing process
    def test_user_editing_routes(self):
        pass

    # Test user deletion process
    def test_user_deletion_routes(self):
        pass

    # Test adding a follower
    def test_adding_follower(self):
        pass
