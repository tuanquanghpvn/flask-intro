from flask.ext.classy import FlaskView
from flask.ext.login import login_required


class LoginRequireMixin(FlaskView):
    decorators = [login_required]
