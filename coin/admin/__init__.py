# -*- coding: utf-8 -*-
from flask import redirect, request, url_for
from flask.ext.admin import Admin
from flask.ext.admin.contrib.sqla import ModelView
from flask.ext.security import current_user
from coin import coin
from coin.models import db, Role, User, Task


class CoinModelView(ModelView):

    def is_accessible(self):

        return current_user.has_role("admin")

    def inaccessible_callback(self, name, **kwargs):

        return redirect(url_for("security.login", next=request.url))


class UserModelView(CoinModelView):

    column_exclude_list = ('password',)

    form_excluded_columns = ('password',)


admin = Admin(coin, name="Coin Dashboard", template_mode="bootstrap3")

admin.add_view(CoinModelView(Role, db.session))
admin.add_view(UserModelView(User, db.session))
admin.add_view(CoinModelView(Task, db.session))

@coin.context_processor
def coin_context_processor():

    return dict()
