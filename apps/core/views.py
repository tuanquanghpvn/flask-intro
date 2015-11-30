from flask.ext.classy import FlaskView
from flask.ext.login import login_required, current_user, logout_user, session


class LoginRequireMixin(FlaskView):
    decorators = [login_required]

    def before_request(self, *args, **kwargs):
        if not current_user.is_active:
            logout_user()
            session.clear()


class AdminRequireMixin(LoginRequireMixin):
    def before_request(self, *args, **kwargs):
        if not current_user.is_staff and not current_user.is_superuser:
            logout_user()
            session.clear()
