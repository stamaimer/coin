# -*- coding: utf-8 -*-
from flask import abort, redirect, request, url_for
from flask.ext.admin import Admin
from flask.ext.admin.contrib.sqla import ModelView
from flask.ext.security import current_user
from coin import coin
from coin.models import db, Role, User, Task


class CoinModelView(ModelView):

    pass

admin = Admin(coin, name="Coin Dashboard", template_mode="bootstrap3")

admin.add_view(CoinModelView(Role, db.session))
admin.add_view(CoinModelView(User, db.session))
admin.add_view(CoinModelView(Task, db.session))

