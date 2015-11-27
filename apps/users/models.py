from flask_user import UserMixin
from apps import db
from apps.core.models import Timestampable


class User(Timestampable, UserMixin):
    __tablename__ = 'users'

    # Require Information
    id = db.Column('user_id', db.Integer, primary_key=True)
    username = db.Column('username', db.String(20), unique=True, index=True)
    password = db.Column('password', db.Text())
    email = db.Column('email', db.String(50), unique=True, index=True)

    # Name Information
    first_name = db.Column('first_name', db.String(255), nullable=False, server_default='')
    last_name = db.Column('last_name', db.String(255), nullable=False, server_default='')
    avatar = db.Column('avatar', db.String(255))

    def __init__(self, username, password, email, firts_name, last_name):
        self.username = username
        self.password = password
        self.email = email
        self.first_name = firts_name
        self.last_name = last_name

