from flask import Blueprint

contacts_bluesrprints = Blueprint('contacts', __name__, template_folder='templates', static_folder='static',
                                  url_prefix='/contact')

from . import views
