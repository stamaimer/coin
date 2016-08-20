# -*- coding: utf-8 -*-

"""

    coin.view
    ~~~~~~~~~

    stamaimer 08/14/16

"""

from datetime import datetime
from flask import Blueprint
from flask import abort, make_response, redirect, render_template, request
from flask_sqlalchemy import get_debug_queries


view = Blueprint("view", __name__)


# @view.before_app_first_request
# def before_first_request():
#
#     pass
#
#
# @view.before_app_request
# def before_request():
#
#     pass
#
#
# @view.after_app_request
# def after_request():
#
#     pass
#
#
# @view.teardown_app_request
# def teardown_request():
#
#     pass


@view.route('/')
def index():

    return render_template("index.html", current_time=datetime.utcnow())


@view.app_errorhandler(404)
def page_not_found():

    pass
