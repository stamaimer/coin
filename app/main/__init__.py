# -*- coding: utf-8 -*-

"""

    coin.app.main
    ~~~~~~~~~~~~~

    stamaimer 08/14/16

"""

from datetime import datetime
from flask import Blueprint
from flask import abort, make_response, redirect, render_template, request
from flask_sqlalchemy import get_debug_queries


main = Blueprint("main", __name__)


@main.before_app_first_request
def before_app_first_request():

    pass


@main.before_app_request
def before_app_request():

    pass


@main.after_app_request
def after_app_request():

    pass


@main.teardown_app_request
def teardown_app_request():

    pass


@main.route('/')
def index():

    return render_template("index.html", current_time=datetime.utcnow())


@main.app_errorhandler(404)
def page_not_found():

    pass
