# -*- coding: utf-8 -*-

"""

    coin.view
    ~~~~~~~~~

    stamaimer 08/14/16

"""

from flask import Blueprint
from flask import abort, make_response, redirect, render_template, request
from flask_sqlalchemy import get_debug_queries


view = Blueprint("view", __name__)


@view.before_first_request
def before_first_request():

    pass


@view.before_request
def before_request():

    pass


@view.after_request
def after_request():

    pass


@view.teardown_request
def teardown_request():

    pass
