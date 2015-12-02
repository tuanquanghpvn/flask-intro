from flask import render_template, request
from flask.ext.classy import FlaskView
from . import contacts_bluesrprints


class ContactView(FlaskView):
    route_base = '/'

    def get_context_data(self):
        context = {
            'info': {
                'title': 'Contact - Clean Blog',
                'head': 'Contact Me',
                'sub': 'Have questions? I have answers (maybe).',
                'image': 'contact-bg.jpg',
            },
        }
        return context

    def index(self):
        context = self.get_context_data()
        return render_template('contacts/index.html', **context)

ContactView.register(contacts_bluesrprints)