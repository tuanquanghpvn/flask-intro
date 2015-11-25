from flask import Blueprint

posts_blueprint = Blueprint('posts', __name__, template_folder='templates', static_folder='static', url_prefix='/post')

from . import views, models
