from unittest import TestCase
from app import app, db
from models import Message


class MessageModelTests(TestCase):
    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.close()
        # db.drop_all()

    def test_message_creation(self):
        new_message = Message(text="This is a test message", user_id=1)
        db.session.add(new_message)
        db.session.commit()

        found_message = Message.query.get(new_message.id)

        self.assertEqual(new_message.text, found_message.text)
        self.assertEqual(new_message.user_id, found_message.user_id)
        self.assertIsNotNone(found_message.timestamp)

    def test_message_deletion(self):
        found_message = Message.query.first()
        found_message_id = found_message.id

        db.session.delete(found_message)
        db.session.commit()

        self.assertIsNone(
            Message.query.filter(id == found_message_id).one_or_none())
