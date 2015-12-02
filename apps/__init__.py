from flask import Flask, request, redirect, url_for
from flask.ext.migrate import Migrate, MigrateCommand
from flask.ext.script import Manager
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.bcrypt import Bcrypt
from flask.ext.login import LoginManager

# Init App
app = Flask(__name__)
app.config.from_object('config.dev')

# SQL Alchemy and Flask Migrate
db = SQLAlchemy(app)
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

# Bcrypt
bcrypt = Bcrypt(app)

# Login manager
login_manager = LoginManager()
login_manager.init_app(app)

# Register blueprint
from .admin import admin_blueprint
from .categories import categories_blueprint
from .posts import posts_blueprint
from .users import users_blueprint

from .homes import homes_bluesrprints
from .contacts import contacts_bluesrprints
from .abouts import abouts_bluesrprints

app.register_blueprint(admin_blueprint)
app.register_blueprint(categories_blueprint)
app.register_blueprint(posts_blueprint)
app.register_blueprint(users_blueprint)

app.register_blueprint(homes_bluesrprints)
app.register_blueprint(contacts_bluesrprints)
app.register_blueprint(abouts_bluesrprints)


@login_manager.unauthorized_handler
def unauthorized_handler():
    if request.blueprint == 'admin':
        return redirect(url_for('admin.LoginView:index', next=request.path))
    else:
        pass

from apps.users.models import User
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)
