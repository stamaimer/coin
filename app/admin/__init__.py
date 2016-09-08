# -*- coding: utf-8 -*-

"""

    coin.app.admin
    ~~~~~~~~~~~~~~

    stamaimer 08/15/16

"""

from flask import redirect, request, url_for
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_security import current_user
from app.model import db
from app.model.role import Role
from app.model.user import User

class SecurityModelView(ModelView):

    def is_accessible(self):

        return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):

        return redirect(url_for("security.login"), next=request.url)


class RoleModelView(SecurityModelView):

    column_labels = dict(name=u"角色", description=u"描述")


class UserModelView(SecurityModelView):

    can_view_details = 1

    column_list = ["email", "active", "confirmed_at", "roles"]

    column_details_list = column_list \
                        + ["login_count", "last_login_at", "last_login_ip", "current_login_at", "current_login_ip"]

    column_filters = column_list

    column_exclude_list = ["password", ]

    form_excluded_columns = list(set(column_details_list) - set(column_list)) + ["confirmed_at"]


admin = Admin(name="PIP Admin", template_mode="bootstrap3")

admin.add_view(UserModelView(User, db.session))
admin.add_view(RoleModelView(Role, db.session))
