from apps import db
from apps.core.models import Timestampable, Describable


class Post(Describable, Timestampable):
    content = db.Column(db.Text, default='')
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    category = db.relationship('Category', backref=db.backref('posts', lazy='dynamic'))

    def __init__(self, name, slug, description, content, category):
        self.name = name
        self.slug = slug
        self.description = description
        self.content = content
        self.category = category

    def __repr__(self):
        return '<Post %r>', self.name