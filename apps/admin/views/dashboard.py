from flask import render_template
from flask.ext.classy import FlaskView
from apps.admin import admin_blueprint


class DashboardView(FlaskView):
    route_base = '/'

    def index(self):
        return render_template('/admin/dashboard.html')


DashboardView.register(admin_blueprint)
