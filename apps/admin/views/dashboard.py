from flask import render_template
from flask.ext.classy import FlaskView, route
from apps.admin import admin_blueprint


class DashboardView(FlaskView):
    route_base = '/'

    def get_context_data(self):
        context = {
            'info': {
                'title': 'Dashboard',
                'sidebar': ['dashboard']
            },
        }
        return context

    def index(self):
        return render_template('/admin/dashboard.html', **self.get_context_data())


DashboardView.register(admin_blueprint)
