from flask import render_template, request
from flask.ext.classy import FlaskView
from sqlalchemy import desc

from . import homes_bluesrprints
from apps.posts.models import Post
from flask.ext.paginate import Pagination


class HomePageView(FlaskView):
    route_base = '/'

    def get_context_data(self):
        context = {
            'info': {
                'title': 'Clean Blog',
                'head': 'Clean Blog',
                'sub': 'Blog for you',
                'image': 'home-bg.jpg',
            },
        }
        return context

    def index(self):
        context = self.get_context_data()

        try:
            page = int(request.args.get('page', 1))
        except ValueError:
            page = 1

        pagination = Pagination(page=page, total=Post.query.count(), per_page=6)
        context['pagination'] = pagination
        if page == 1:
            context['object_list'] = Post.query.order_by(desc(Post.id)).limit(6)
        else:
            offset = (page - 1) * 6
            context['object_list'] = Post.query.order_by(desc(Post.id)).offset(offset).limit(6)
        return render_template('homes/index.html', **context)

HomePageView.register(homes_bluesrprints)