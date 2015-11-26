from apps import db
from apps.core.models import Timestampable, Describable


class Category(Describable, Timestampable):
    def __init__(self, name, slug, description):
        self.name = name
        self.slug = slug
        self.description = description

    def __repr__(self):
        return '<Category %r>', self.name
