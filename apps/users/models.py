from flask.ext.login import UserMixin
from apps import db, bcrypt
from apps.core.models import Timestampable


class User(Timestampable, UserMixin):
    # Require Information
    id = db.Column('user_id', db.Integer, primary_key=True)
    username = db.Column('username', db.String(20), unique=True, index=True)
    password = db.Column('password', db.Text())
    email = db.Column('email', db.String(50), unique=True, index=True)

    is_superuser = db.Column('is_superuser', db.Boolean(), nullable=False, default=False)
    is_active = db.Column('is_active', db.Boolean(), nullable=False, default=False)
    is_staff = db.Column('is_staff', db.Boolean(), nullable=False, default=False)

    # Name Information
    first_name = db.Column('first_name', db.String(255), nullable=False, server_default='')
    last_name = db.Column('last_name', db.String(255), nullable=False, server_default='')
    avatar = db.Column('avatar', db.String(255))

    def __init__(self, username, email, password=None, first_name='', last_name='', avatar=None, is_superuser=False,
                 is_active=False, is_staff=False):
        self.username = username
        if password:
            self.password = password
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.avatar = avatar
        self.is_superuser = is_superuser
        self.is_active = is_active
        self.is_staff = is_staff

    def set_password(self, password):
        try:
            pw_hash = bcrypt.generate_password_hash(password)
            self.password = pw_hash
        except:
            raise ValueError("Can't set password!")

    def check_password(self, password):
        try:
            return bcrypt.check_password_hash(self.password, password)
        except:
            return False
