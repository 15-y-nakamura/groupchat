from werkzeug.security import generate_password_hash, check_password_hash
from app import db, login_manager
from flask_login import UserMixin
from sqlalchemy import and_

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class Friend(db.Model):
    __tablename__ = 'friends'
    sender = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
    receiver = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)

    @classmethod
    def is_friend(cls, user1, user2):
        res1 = cls.query.filter(
            and_(
                cls.sender == user1.id,
                cls.receiver == user2.id
            )
        ).first()
        res2 = cls.query.filter(
            and_(
                cls.sender == user2.id,
                cls.receiver == user1.id
            )
        ).first()
        return res1 is not None and res2 is not None

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, index=True)
    email = db.Column(db.String, unique=True, index=True)
    password_hash = db.Column(db.String)
    code = db.Column(db.String, unique=True, nullable=True)
    chat_room = db.relationship('ChatRoom', backref='user')
    send = db.relationship('Friend', foreign_keys=[Friend.sender], backref='send')
    receive = db.relationship('Friend', foreign_keys=[Friend.receiver], backref='receive')

    @property
    def password(self):
        raise AttributeError('パスワードは読み取り可能ではありません')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

class Message(db.Model):
    __tablename__ = 'messages'
    id = db.Column(db.Integer, primary_key=True)
    from_ = db.Column(db.Integer, unique=False, nullable=False)
    to_ = db.Column(db.Integer, unique=False, nullable=False)
    body = db.Column(db.String)
    
class ChatRoom(db.Model):
    __tablename__ = 'chatrooms'
    __table_args__ = (db.UniqueConstraint('name', 'username', name='name_username'),)
    name = db.Column(db.String, primary_key=True)
    messages = db.relationship('GroupMessage', cascade='delete')
    username = db.Column(db.String, db.ForeignKey('users.username'), primary_key=True)

class GroupMessage(db.Model):
    __tablename__ = 'groupmessages'
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String)
    username = db.Column(db.String, db.ForeignKey('users.username'))
    chatroom = db.Column(db.String, db.ForeignKey('chatrooms.name'))
