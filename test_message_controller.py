from unittest import TestCase
from app import db, app, connect_to_db
from flask_login import login_user
from models import Message, User, example_data

connect_to_db(app, db_uri="postgres://localhost/warbler_db_test")


class MessageControllerTests(TestCase):
    def setUp(self):
        db.create_all()
        example_data()

    def tearDown(self):
        db.session.close()
        db.drop_all()

    # Test message creation pro
    # cess (when a form is submitted,
    # the proper information is displayed)
    def test_message_creation_route(self):

        # need to be logged in as an authenticated user
        client = app.test_client()
        user = User.authenticate('booboo1', 'iloveclowns')
        login_user(user)

        # login_result = client.post(ß
        #     '/login',
        #     data={
        #         'username': 'booboo1',
        #         'password': 'iloveclowns'
        #     },
        #     follow_redirects=True)
        # self.assertIn(b'Hello', login_result.data)

        create_message_result = client.post(
            '/users/1/messages',
            data={'text': 'This is a test message!!!!!'},
            follow_redirects=True)
        self.assertIn(b'This is a test message!!!!!',
                      create_message_result.data)

    # Test message deletion process
    def test_message_deletion_route(self):
        pass
