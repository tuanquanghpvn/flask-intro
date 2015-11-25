from flask import Flask
from flask.ext.migrate import Migrate, MigrateCommand
from flask.ext.script import Manager
from flask.ext.sqlalchemy import SQLAlchemy

# Init App
app = Flask(__name__)
app.config.from_object('config.dev')

# SQL Alchemy and Flask Migrate
db = SQLAlchemy(app)
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)


# Register blueprint
from admin import admin_blueprint
from categories import categories_blueprint
from posts import posts_blueprint

app.register_blueprint(admin_blueprint)
app.register_blueprint(categories_blueprint)
app.register_blueprint(posts_blueprint)
