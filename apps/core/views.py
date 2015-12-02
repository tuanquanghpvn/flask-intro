from flask.ext.classy import FlaskView
from flask.ext.login import current_user, current_app
from functools import wraps


def login_required(func):
    """
        Decorator check required login and active user
        :param func:
        :return:
    """
    @wraps(func)
    def decorated_view(*args, **kwargs):
        if current_app.login_manager._login_disabled:
            return func(*args, **kwargs)
        elif not current_user.is_authenticated and not current_user.is_active:
            return current_app.login_manager.unauthorized()
        return func(*args, **kwargs)

    return decorated_view


def admin_required(func):
    """
        Decorator check required login and hava staff or superuser permission
        :param func:
        :return:
    """

    @wraps(func)
    def decorated_view(*args, **kwargs):
        if current_app.login_manager._login_disabled:
            return func(*args, **kwargs)
        elif not current_user.is_authenticated and not current_user.is_active:
            return current_app.login_manager.unauthorized()
        elif not current_user.is_staff and not current_user.is_superuser:
            return current_app.login_manager.unauthorized()
        return func(*args, **kwargs)

    return decorated_view


class LoginRequireMixin(FlaskView):
    decorators = [login_required]


class AdminRequireMixin(LoginRequireMixin):
    decorators = [admin_required]
