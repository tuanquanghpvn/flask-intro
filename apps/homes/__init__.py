from flask import Blueprint

homes_bluesrprints = Blueprint('homes', __name__, template_folder='templates', static_folder='static', url_prefix='/')

from . import views