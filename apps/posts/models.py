from apps import db


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    slug = db.Column(db.String(255))
    category_id = db.ForeignKey('category.id')
    category = db.relationship('Category', backref=db.backref('posts', lazy='dynamic'))

    def __init__(self, name, slug, category):
        self.name = name
        self.slug = slug
        self.category = category

    def __repr__(self):
        return '<Post %r>', self.name