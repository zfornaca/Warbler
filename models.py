from datetime import datetime
from app import db, bcrypt
from flask_login import UserMixin


class Message(db.Model):

    __tablename__ = 'messages'

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow())
    user_id = db.Column(db.Integer,
                        db.ForeignKey('users.id', ondelete='CASCADE'))

    def is_liked_by(self, current_user):
        return bool(self.likers.filter_by(id=current_user.id).first())


FollowersFollowee = db.Table(
    'follows', db.Column('id', db.Integer, primary_key=True),
    db.Column('followee_id', db.Integer,
              db.ForeignKey('users.id', ondelete="cascade")),
    db.Column('follower_id', db.Integer,
              db.ForeignKey('users.id', ondelete="cascade")),
    db.CheckConstraint('follower_id != followee_id', name="no_self_follow"))

Likes = db.Table(
    'likes', db.Column('id', db.Integer, primary_key=True),
    db.Column('user_id', db.Integer,
              db.ForeignKey('users.id', ondelete="cascade")),
    db.Column('message_id', db.Integer,
              db.ForeignKey('messages.id', ondelete="cascade")))


class User(db.Model, UserMixin):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.Text, unique=True)
    username = db.Column(db.Text, unique=True)
    image_url = db.Column(db.Text, default="/static/images/default-pic.png")
    header_image_url = db.Column(db.Text)
    bio = db.Column(db.Text)
    location = db.Column(db.Text)
    password = db.Column(db.Text)
    messages = db.relationship('Message', backref='user', lazy='dynamic')
    likes = db.relationship(
        'Message',
        secondary=Likes,
        backref=db.backref('likers'),
        lazy='dynamic')
    followers = db.relationship(
        "User",
        secondary=FollowersFollowee,
        primaryjoin=(FollowersFollowee.c.follower_id == id),
        secondaryjoin=(FollowersFollowee.c.followee_id == id),
        backref=db.backref('following', lazy='dynamic'),
        lazy='dynamic')

    def __repr__(self):
        return f"User #{self.id}: email: {self.email} - username: {self.username}"

    def is_followed_by(self, user):
        return bool(self.followers.filter_by(id=user.id).first())

    def is_following(self, user):
        return bool(self.following.filter_by(id=user.id).first())

    def is_liking(self, message):
        return bool(self.likes.filter_by(id=message.id).first())

    @staticmethod
    def hash_password(plaintext_pw):
        return bcrypt.generate_password_hash(plaintext_pw).decode('UTF-8')

    @classmethod
    def authenticate(cls, username, password):
        found_user = cls.query.filter_by(username=username).first()
        if found_user:
            is_authenticated = bcrypt.check_password_hash(
                found_user.password, password)
            if is_authenticated:
                return found_user
        return False


def example_data():
    """Function to add simple data to the test database."""

    # iloveclowns
    u1 = User(
        email='booboo@email.com',
        username='booboo1',
        password=User.hash_password('iloveclowns'),
        bio='I LIVE IN A CIRCUS',
        location='The Center Ring')

    u2 = User(
        email='Ariel@underthesea.com',
        username='mermaid88',
        password=User.hash_password('dinglehopper'),
        bio='Chicken of the sea',
        location="King Triton's Kingdom")
    u3 = User(
        email='Whiskey@dogbook.com',
        username='ILOVEFOOD',
        password=User.hash_password('treats'),
        bio="GIMME FOOD",
        location="rithm")

    m1 = Message(text="Hey everybody I'm a clown", user_id=1)
    m2 = Message(text="I wanna be where the people are", user_id=2)
    m3 = Message(text="FOOD FOOD FOOD", user_id=3)

    db.session.add(u1)
    db.session.add(u2)
    db.session.add(u3)
    db.session.add(m1)
    db.session.add(m2)
    db.session.add(m3)

    db.session.commit()


db.create_all()
