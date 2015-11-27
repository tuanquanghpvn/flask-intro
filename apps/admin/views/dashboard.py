from flask import render_template
from flask.ext.classy import FlaskView
from apps.admin import admin_blueprint
from apps.core.views import LoginRequireMixin


class LoginView(FlaskView):
    route_base = '/login'

    def get_context_data(self):
        context = {
            'info': {
                'title': 'Administrator'
            },
        }
        return context

    def index(self):
        return render_template('/admin/login.html', **self.get_context_data())

    def post(self):
        pass


LoginView.register(admin_blueprint)


class LogoutView(FlaskView):
    def index(self):
        pass


LogoutView.register(admin_blueprint)


class DashboardView(LoginRequireMixin):
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
