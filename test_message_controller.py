from unittest import TestCase
from app import db, app, connect_to_db
from models import Message, User, example_data

connect_to_db(app, db_uri="postgres://localhost/warbler_db_test")


class MessageControllerTests(TestCase):
    def setUp(self):
        db.create_all()
        example_data()

    def tearDown(self):
        db.session.close()
        db.drop_all()

    # def test_add_user(self):
    #     new_user = User(email="joel@joel.com")
    #     db.session.add(new_user)
    #     db.session.commit()

    # def test_joel_not_there(self):
    #     self.assertEqual(
    #         User.query.filter_by(email="joel@joel.com").first(), None)

    # Test message creation pro
    # cess (when a form is submitted,
    # the proper information is displayed)
    def test_message_creation_route(self):

        # need to be logged in as an authenticated user
        client = app.test_client()
        result = client.post(
            '/users/1/messages',
            data={'text': 'This is a test message!!!!!'},
            follow_redirects=True)
        self.assertIn(b'This is a test message!!!!!', result.data)

    # Test message deletion process
    def test_message_deletion_route(self):
        pass
