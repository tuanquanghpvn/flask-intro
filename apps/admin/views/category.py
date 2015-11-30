from flask import render_template, redirect, url_for
from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired, Regexp
from apps import db
from apps.core.views import LoginRequireMixin
from apps.admin import admin_blueprint
from apps.categories.models import Category


class CategoryForm(Form):
    """
        Form View Category
    """
    name = StringField('name', validators=[DataRequired()])
    slug = StringField('slug', validators=[DataRequired(), Regexp(r'[\w-]+$', message='Slug is not validate!')])
    description = StringField('description')


class CategoryListView(LoginRequireMixin):
    """
        Show List Category
        Paginate Category
    """
    route_base = '/category'

    def get_context_data(self):
        context = {
            'info': {
                'title': 'Category List',
                'sidebar': ['category']
            },
            'object_list': Category.query.all(),
        }
        return context

    def index(self):
        return render_template('/admin/category_index.html', **self.get_context_data())


CategoryListView.register(admin_blueprint)


class CategoryCreateView(LoginRequireMixin):
    """
        Create Category
    """
    route_base = '/category/create'

    def get_context_data(self):
        context = {
            'info': {
                'title': 'Category Create',
                'sidebar': ['category']
            },
            'form': CategoryForm()
        }
        return context

    def index(self):
        return render_template('/admin/category_create.html', **self.get_context_data())

    def post(self):
        form = CategoryForm()
        if form.validate_on_submit():
            category = Category(
                name=form.name.data,
                slug=form.slug.data,
                description=form.description.data
            )
            db.session.add(category)
            db.session.commit()
            return redirect(url_for('admin.CategoryListView:index'))
        else:
            context = self.get_context_data()
            context['form'] = form
            return render_template('/admin/category_create.html', **context)


CategoryCreateView.register(admin_blueprint)


class CategoryUpdateView(LoginRequireMixin):
    """
       Update Category
    """
    route_base = '/category/update/<id>'

    def get_context_data(self):
        context = {
            'info': {
                'title': 'Category Update',
                'sidebar': ['category']
            },
            'form': CategoryForm()
        }
        return context

    def get(self, id):
        category = Category.query.get(id)
        context = self.get_context_data()
        context['form'] = CategoryForm(obj=category)
        return render_template('/admin/category_update.html', **context)

    def post(self, id):
        form = CategoryForm()
        if form.validate_on_submit():
            category = Category.query.get(id)
            category.name = form.name.data
            category.slug = form.slug.data
            category.description = form.description.data

            db.session.commit()
            return redirect(url_for('admin.CategoryListView:index'))
        else:
            context = self.get_context_data()
            context['form'] = form
            return render_template('/admin/category_update.html', **context)


CategoryUpdateView.register(admin_blueprint)


class CategoryDeleteView(LoginRequireMixin):
    """
        Delete Category
    """
    route_base = '/category/delete/<id>'

    def get(self, id):
        try:
            category = Category.query.get(id)
            db.session.delete(category)
            db.session.commit()
            return redirect(url_for('admin.CategoryListView:index'))
        except:
            return redirect(url_for('admin.CategoryListView:index'))


CategoryDeleteView.register(admin_blueprint)
