from flask import render_template, redirect, url_for
from flask_wtf import Form
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Regexp, Email, EqualTo
from apps import db
from apps.core.views import AdminRequireMixin
from apps.admin import admin_blueprint
from apps.users.models import User


class UserForm(Form):
    """
        Form View User
    """
    username = StringField('username', validators=[DataRequired()])
    password1 = PasswordField('password1', validators=[DataRequired()])
    password2 = PasswordField('password2', validators=[DataRequired(),
                                                       EqualTo('password1', message='Re password not equal password!')])
    email = StringField('email', validators=[DataRequired(), Email()])
    first_name = StringField('first_name')
    last_name = StringField('last_name')

    def validate(self):
        rv = Form.validate(self)
        if not rv:
            return False
        username = User.query.filter_by(username=self.username.data).first()
        email = User.query.filter_by(email=self.email.data).first()
        if username:
            self.username.errors.append('Username is already exit!')
            return False
        if email:
            self.email.errors.append('Email is already exit!')
            return False
        if self.password1 == self.password2:
            self.password2.errors.append('Re password is not equal password!')
            return False
        return True


class UserListView(AdminRequireMixin):
    """
        Show List User
        Paginate User
    """
    route_base = '/user'

    def get_context_data(self):
        context = {
            'info': {
                'title': 'User List',
                'sidebar': ['user']
            },
            'object_list': User.query.all(),
        }
        return context

    def index(self):
        return render_template('/admin/user_index.html', **self.get_context_data())


UserListView.register(admin_blueprint)


class UserCreateView(AdminRequireMixin):
    """
        Create User
    """
    route_base = '/user/create'

    def get_context_data(self):
        context = {
            'info': {
                'title': 'User Create',
                'sidebar': ['user']
            },
            'form': UserForm()
        }
        return context

    def index(self):
        return render_template('/admin/user_create.html', **self.get_context_data())

    def post(self):
        form = UserForm()
        if form.validate_on_submit():
            user = User(
                username=form.username.data,
                email=form.email.data,
                first_name=form.first_name.data,
                last_name=form.last_name.data,
                avatar='',
                active=True
            )
            user.set_password(form.password1.data)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('admin.UserListView:index'))
        else:
            context = self.get_context_data()
            context['form'] = form
            return render_template('/admin/user_create.html', **context)


UserCreateView.register(admin_blueprint)


class UserUpdateView(AdminRequireMixin):
    """
       Update User
    """
    route_base = '/user/update/<id>'

    def get_context_data(self):
        context = {
            'info': {
                'title': 'User Update',
                'sidebar': ['user']
            },
            'form': UserForm()
        }
        return context

    def get(self, id):
        user = User.query.get(id)
        context = self.get_context_data()
        context['form'] = UserForm(obj=user)
        return render_template('/admin/user_update.html', **context)

    def post(self, id):
        form = UserForm()
        if form.validate_on_submit():
            user = User.query.get(id)
            user.name = form.name.data
            user.slug = form.slug.data
            user.description = form.description.data

            db.session.commit()
            return redirect(url_for('admin.UserListView:index'))
        else:
            context = self.get_context_data()
            context['form'] = form
            return render_template('/admin/user_update.html', **context)


UserUpdateView.register(admin_blueprint)


class UserDeleteView(AdminRequireMixin):
    """
        Delete User
    """
    route_base = '/user/delete/<id>'

    def get(self, id):
        try:
            user = User.query.get(id)
            db.session.delete(user)
            db.session.commit()
            return redirect(url_for('admin.UserListView:index'))
        except:
            return redirect(url_for('admin.UserListView:index'))


UserDeleteView.register(admin_blueprint)
