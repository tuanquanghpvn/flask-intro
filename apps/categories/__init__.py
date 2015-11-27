from flask import Blueprint

categories_blueprint = Blueprint('categories', __name__, template_folder='templates', static_folder='static',
                                 url_prefix='/category')

from . import models, views
