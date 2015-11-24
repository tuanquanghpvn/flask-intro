from flask import Blueprint, render_template

admin = Blueprint( 'admin', __name__,
                    template_folder='templates',
                    static_folder='static',)

from . import views
