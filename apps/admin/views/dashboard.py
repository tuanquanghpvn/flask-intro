from flask import render_template, redirect, url_for, session
from flask.ext.classy import FlaskView
from flask.ext.login import logout_user
from flask_wtf import Form
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired
from apps.admin import admin_blueprint
from apps.core.views import LoginRequireMixin
from apps.users.models import User


class LoginForm(Form):
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])

    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)
        self.user = None

    def validate(self):
        rv = Form.validate(self)
        if not rv:
            return False
        if not self.username.data or not self.password.data:
            return False
        user = User.query.filter_by(username=self.username.data).first()
        if user is None:
            self.username.errors.append('Unknown username')
            return False
        if not user.check_password(self.password.data):
            self.password.errors.append('Invalid password')
            return False
        self.user = user
        return True


class LoginView(FlaskView):
    route_base = '/login'

    def get_context_data(self):
        context = {
            'info': {
                'title': 'Administrator'
            },
            'form': LoginForm()
        }
        return context

    def index(self):
        return render_template('/admin/login.html', **self.get_context_data())

    def post(self):
        form = LoginForm()
        if form.validate_on_submit():
            session['user_id'] = form.user.id
            return redirect(url_for('admin.DashboardView:index'))
        else:
            context = self.get_context_data()
            context['form'] = form
            return render_template('/admin/login.html', **context)


LoginView.register(admin_blueprint)


class LogoutView(LoginRequireMixin):
    route_base = '/logout'

    def index(self):
        logout_user()
        session.clear()
        return redirect(url_for('admin.LoginView:index'))


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
