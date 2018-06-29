from unittest import TestCase
from app import db, app, connect_to_db
from models import User, example_data

connect_to_db(app, db_uri="postgres://localhost/warbler_db_test")


class UserControllerTests(TestCase):
    def setUp(self):
        db.create_all()
        example_data()
        app.config['WTF_CSRF_ENABLED'] = False

    def tearDown(self):
        db.session.close()
        db.drop_all()

    # Test that a user who isn't logged in cannot access routes
    # requiring a login
    def test_authenticated_routes(self):
        client = app.test_client()
        response = client.get('/users/1/following', follow_redirects=True)
        print(response.data)
        self.assertIn(b'Welcome back.', response.data)

    # Test user creation process (i.e. after form is submitted,
    # a user's info is properly displayed on profile page)
    def test_user_creation_routes(self):
        client = app.test_client()
        response = client.post(
            '/signup',
            data={
                'username': 'mailydude',
                'email': 'maily@email.com',
                'password': 'emailme'
            },
            follow_redirects=True)
        self.assertIn(b'@mailydude', response.data)

    # Test user editing process
    def test_user_editing_routes(self):
        client = app.test_client()
        login_result = client.post(
            '/login',
            data={
                'username': 'booboo1',
                'password': 'iloveclowns'
            },
            follow_redirects=True)

        response = client.patch(
            '/users/1',
            data={
                'username': 'mailyd00d',
                'email': 'maily@email.com',
                'password': 'iloveclowns'
            },
            follow_redirects=True)
        self.assertIn(b'@mailyd00d', response.data)

    # Test user deletion process
    # def test_user_deletion_routes(self):
    #     client = app.test_client()
    #     login_result = client.post(
    #         '/login',
    #         data={
    #             'username': 'booboo1',
    #             'password': 'iloveclowns'
    #         },
    #         follow_redirects=True)

    #     response = client.delete('/users/1', follow_redirects=True)
    # self.assertNotIn(b'@', response.data)

    # Test adding a follower
    def test_adding_follower(self):
        pass
