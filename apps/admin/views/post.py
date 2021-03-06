from flask import render_template, redirect, url_for
from flask.ext.uploads import UploadSet, IMAGES
from flask_wtf import Form
from flask_wtf.file import FileAllowed
from flask_wtf.file import FileField
from werkzeug.utils import secure_filename
from wtforms import StringField, SelectField
from wtforms.validators import DataRequired, Regexp, InputRequired
from apps import db, app
from apps.admin import admin_blueprint
from apps.categories.models import Category
from apps.posts.models import Post
from apps.core.views import AdminRequireMixin
import os


class PostForm(Form):
    """
        Form View Post
    """
    category_id = SelectField('category', coerce=int, choices=[(item.id, item.name) for item in Category.query.all()],
                              validators=[InputRequired()])
    name = StringField('name', validators=[DataRequired()])
    slug = StringField('slug', validators=[DataRequired(), Regexp(r'[\w-]+$', message='Slug is not validate!')])
    description = StringField('description')
    content = StringField('content')
    image = FileField('image')


class PostListView(AdminRequireMixin):
    """
        Show List Post
        Paginate Post
    """
    route_base = '/post'

    def get_context_data(self):
        context = {
            'info': {
                'title': 'Post List',
                'sidebar': ['post']
            },
            'object_list': Post.query.all(),
        }
        return context

    def index(self):
        return render_template('/admin/post_index.html', **self.get_context_data())


PostListView.register(admin_blueprint)


class PostCreateView(AdminRequireMixin):
    """
        Create Post
    """
    route_base = '/post/create'

    def get_context_data(self):
        context = {
            'info': {
                'title': 'Post Create',
                'sidebar': ['post']
            },
            'form': PostForm(),
        }
        return context

    def index(self):
        return render_template('/admin/post_create.html', **self.get_context_data())

    def post(self):
        form = PostForm()
        if form.validate_on_submit():
            post = Post(
                name=form.name.data,
                slug=form.slug.data,
                description=form.description.data,
                content=form.content.data,
                category_id=form.category_id.data
            )
            if form.image.data:
                filename = secure_filename(form.image.data.filename)
                dir_save = os.path.join('media/posts/', filename)
                form.image.data.save(dir_save)
                post.image = dir_save
            db.session.add(post)
            db.session.commit()
            return redirect(url_for('admin.PostListView:index'))
        else:
            context = self.get_context_data()
            context['form'] = form
            return render_template('/admin/post_create.html', **context)


PostCreateView.register(admin_blueprint)


class PostUpdateView(AdminRequireMixin):
    """
       Update Post
    """
    route_base = '/post/update/<id>'

    def get_context_data(self):
        context = {
            'info': {
                'title': 'Post Update',
                'sidebar': ['post']
            },
            'form': PostForm()
        }
        return context

    def get(self, id):
        post = Post.query.get(id)
        context = self.get_context_data()
        context['form'] = PostForm(obj=post)
        return render_template('/admin/post_update.html', **context)

    def post(self, id):
        form = PostForm()
        if form.validate_on_submit():
            post = Post.query.filter_by(id=id).first()

            post.category_id = form.category_id.data
            post.name = form.name.data
            post.slug = form.slug.data
            post.description = form.description.data
            post.content = form.content.data

            db.session.commit()
            return redirect(url_for('admin.PostListView:index'))
        else:
            context = self.get_context_data()
            context['form'] = form
            return render_template('/admin/post_update.html', **context)


PostUpdateView.register(admin_blueprint)


class PostDeleteView(AdminRequireMixin):
    """
        Delete Post
    """
    route_base = '/post/delete/<id>'

    def get(self, id):
        try:
            post = Post.query.get(id)
            db.session.delete(post)
            db.session.commit()
            return redirect(url_for('admin.PostListView:index'))
        except:
            return redirect(url_for('admin.PostListView:index'))


PostDeleteView.register(admin_blueprint)
