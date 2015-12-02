from flask import render_template, request
from flask.ext.classy import FlaskView
from . import abouts_bluesrprints


class AboutView(FlaskView):
    route_base = '/'

    def get_context_data(self):
        context = {
            'info': {
                'title': 'Clean Blog - About',
                'head': 'About Me',
                'sub': 'This is what I do.',
                'image': 'about-bg.jpg',
            },
        }
        return context

    def index(self):
        context = self.get_context_data()

        return render_template('abouts/index.html', **context)

AboutView.register(abouts_bluesrprints)