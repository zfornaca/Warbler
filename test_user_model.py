from unittest import TestCase
from app import db, app, connect_to_db
from models import User, example_data

connect_to_db(app, db_uri="postgres://localhost/warbler_db_test")


class UserModelTests(TestCase):
    def setUp(self):
        db.create_all()
        example_data()

    def tearDown(self):
        db.session.close()
        db.drop_all()

    def test_user_creation(self):
        new_user = User(
            email='booboo2@email.com',
            username='booboo2',
            password='iloveclownsmorethanyou',
            bio='I live in a circus',
            location='coney island')
        db.session.add(new_user)
        db.session.commit()

        found_user = User.query.get(new_user.id)

        self.assertEqual(new_user.email, found_user.email)
        self.assertEqual(new_user.username, found_user.username)
        self.assertIsNotNone(found_user.password)

    def test_user_deletion(self):
        found_user = User.query.first()
        found_user_id = found_user.id

        db.session.delete(found_user)
        db.session.commit()

        self.assertIsNone(User.query.filter(id == found_user_id).one_or_none())

    # Test user authenticate method