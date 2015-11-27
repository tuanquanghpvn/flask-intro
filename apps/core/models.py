from apps import db


class Describable(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255))
    slug = db.Column(db.String(255))
    description = db.Column(db.Text)


class Timestampable(db.Model):
    __abstract__ = True

    created_date = db.Column(db.DateTime, default=db.func.now())
    modified_date = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())
