from coin import admin, db, current_user
from coin.models import *
from flask import abort, redirect, request, url_for
from flask.ext.admin.contrib.sqla import ModelView


class CoinModelView(ModelView):

    def is_accessible(self):

        if not current_user.is_active or not current_user.is_authenticated:

            return False

        if current_user.has_role("admin"):

            return True

        return False

    def _handle_view(self, name, **kwargs):

        if not self.is_accessible():

            if not current_user.is_authenticated:

                abort(403)

            else:

                return redirect(url_for("security.login", next=request.url))

admin.add_view(ModelView(Role, db.session))
admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Task, db.session))