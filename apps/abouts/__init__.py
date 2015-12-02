from flask import Blueprint

abouts_bluesrprints = Blueprint('abouts', __name__, template_folder='templates', static_folder='static',
                                url_prefix='/about')

from . import views
