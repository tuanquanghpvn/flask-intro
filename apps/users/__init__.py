from flask import Blueprint

users_blueprint = Blueprint('users', __name__, static_folder='static', template_folder='templates', url_prefix='/user')

from . import views, models
