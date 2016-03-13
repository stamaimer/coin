# -*- coding: utf-8 -*-
from flask.ext.admin import Admin
from flask.ext.admin.contrib.sqla import ModelView
from coin import coin
from coin.models import db, Role, User, Task


class CoinModelView(ModelView):

    pass

admin = Admin(coin, name="Coin Dashboard", template_mode="bootstrap3")

admin.add_view(ModelView(Role, db.session))
admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Task, db.session))

