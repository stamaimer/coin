# -*- coding: utf-8 -*-

"""

    coin.app.admin
    ~~~~~~~~~~~~~~

    stamaimer 08/15/16

"""

from flask import redirect, request, url_for, current_app
from flask_admin import Admin, form,expose
from flask_admin.contrib.sqla import ModelView
from flask_security import current_user
from sqlalchemy.event import listens_for
from app.model import db
from app.model.pip_user import Pip_user
from app.model.resource import Resource
from app.model.cv import Cv
from app.model.news import News
from app.model.pip_block import Pip_block
from app.model.podcast import Podcast
from app.model.portfolio import Portfolio
import os
import os.path as op
file_path = './app/static/upload'

# from app.model.role import Role
# from app.model.user import User


@listens_for(Resource, 'after_delete')
def del_file(mapper, connection, target):
    if target.path:
        try:
            os.remove(op.join(file_path, target.path))
        except OSError:
            # Don't care if was not deleted because it does not exist
            pass


class SecurityModelView(ModelView):
    # def is_accessible(self):
    #     return current_user.is_authenticated
    #
    # def inaccessible_callback(self, name, **kwargs):
    #     return redirect(url_for("security.login"), next=request.url)
    pass


class PipUserView(SecurityModelView):
    can_view_details = 1

    column_list = ["email", "password", "name", "title", "department"]

    column_details_list = column_list + ["access_code", "info", "photo", "video", "podcast", "cv", "news", "portfolio",
                                         "pip_block"]

    column_filters = column_list


class ResourceView(SecurityModelView):
    form_overrides = {'path': form.FileUploadField}

    # Pass additional parameters to 'path' to FileUploadField constructor
    form_args = {'path': {'label': 'File', 'base_path': file_path, 'allow_overwrite': False}}

    form_choices = {'type': [('p', 'Picture'), ('v', 'Video'), ('a', 'Audio')]}


# class RoleModelView(SecurityModelView):
#     column_labels = dict(name=u"角色", description=u"描述")
#
#
# class UserModelView(SecurityModelView):
#     can_view_details = 1
#
#     column_list = ["email", "active", "confirmed_at", "roles"]
#
#     column_details_list = column_list + ["login_count", "last_login_at", "last_login_ip", "current_login_at",
#                                          "current_login_ip"]
#
#     column_filters = column_list
#
#     column_exclude_list = ["password", ]
#
#     form_excluded_columns = list(set(column_details_list) - set(column_list)) + ["confirmed_at"]


admin = Admin(name="PIP Admin", template_mode="bootstrap3")

admin.add_view(PipUserView(Pip_user, db.session, name='User'))
admin.add_view(ResourceView(Resource, db.session, name='Resource'))
admin.add_view(SecurityModelView(Cv, db.session, name='CV'))
admin.add_view(SecurityModelView(News, db.session, name='News'))
admin.add_view(SecurityModelView(Pip_block, db.session, name='Block'))
admin.add_view(SecurityModelView(Podcast, db.session, name='Podcast'))
admin.add_view(SecurityModelView(Portfolio, db.session, name='Portfolio'))
