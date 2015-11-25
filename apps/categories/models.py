from apps import db


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255))
    slug = db.Column(db.String(255))

    def __init__(self, name, slug):
        self.name = name
        self.slug = slug

    def __repr__(self):
        return '<Category %r>', self.name
