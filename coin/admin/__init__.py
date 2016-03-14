# -*- coding: utf-8 -*-
from flask import abort, redirect, request, url_for
from flask.ext.admin import Admin
from flask.ext.admin.contrib.sqla import ModelView
from flask.ext.security import current_user
from coin import coin
from coin.models import db, Role, User, Task


class CoinModelView(ModelView):

    def is_accessible(self):
        if not current_user.is_active or not current_user.is_authenticated:
            return False

        if current_user.has_role('superuser'):
            return True

        return False

    def _handle_view(self, name, **kwargs):
        """
        Override builtin _handle_view in order to redirect users when a view is not accessible.
        """
        if not self.is_accessible():
            if current_user.is_authenticated:
                # permission denied
                abort(403)
            else:
                # login
                return redirect(url_for('security.login', next=request.url))

admin = Admin(coin, name="Coin Dashboard", template_mode="bootstrap3")

admin.add_view(CoinModelView(Role, db.session))
admin.add_view(CoinModelView(User, db.session))
admin.add_view(CoinModelView(Task, db.session))

