from flask import render_template, redirect, url_for, session, request
from flask.ext.classy import FlaskView
from flask.ext.login import logout_user
from flask_wtf import Form
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, EqualTo
from apps import db
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
    """
        Dashboard View
    """
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


class ProfileForm(Form):
    """
        Profile Form: Change password form
    """
    old_password = PasswordField('old_password', validators=[DataRequired()])
    password1 = PasswordField('password1', validators=[DataRequired()])
    password2 = PasswordField('password2', validators=[DataRequired(),
                                                       EqualTo('password1', message='Re password not equal password!')])

    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)
        self.user = None

    def validate(self):
        rv = Form.validate(self)
        if not rv:
            return False
        user = User.query.filter_by(id=session['user_id']).first()
        if not user.check_password(self.old_password.data):
            self.old_password.errors.append('Invalid old password!')
            return False
        self.user = user
        return True


class ProfileView(LoginRequireMixin):
    """
        Profile View: Change password
    """
    route_base = '/profile'

    def get_context_data(self):
        context = {
            'info': {
                'title': 'Change Profile',
                'sidebar': ['dashboard']
            },
            'form': ProfileForm(),
        }
        return context

    def index(self):
        return render_template('/admin/profile.html', **self.get_context_data())

    def post(self):
        form = ProfileForm()
        if form.validate_on_submit():
            user = form.user
            user.set_password(form.password1.data)
            db.session.commit()

            # Logout and redirect to login page
            logout_user()
            session.clear()
            return redirect(url_for('admin.LoginView:index'))
        else:
            context = self.get_context_data()
            context['form'] = form
            return render_template('/admin/profile.html', **context)


ProfileView.register(admin_blueprint)