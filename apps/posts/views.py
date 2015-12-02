from flask import render_template, request
from flask.ext.classy import FlaskView
from . import posts_blueprint
from apps.posts.models import Post


class DetailPostView(FlaskView):
    route_base = '/<id>-<slug>'

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

    def get(self, id, slug):
        context = self.get_context_data()
        post = Post.query.get(id)
        context['object'] = post
        context['info']['title'] = post.name
        context['info']['head'] = post.name
        context['info']['sub'] = post.description
        return render_template('posts/detail.html', **context)


DetailPostView.register(posts_blueprint)
