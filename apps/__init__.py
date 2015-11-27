from flask import Flask
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

app.register_blueprint(admin_blueprint)
app.register_blueprint(categories_blueprint)
app.register_blueprint(posts_blueprint)
app.register_blueprint(users_blueprint)