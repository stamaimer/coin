# -*- coding: utf-8 -*-

"""

    coin.view
    ~~~~~~~~~

    stamaimer 08/14/16

"""

from flask import Blueprint
from flask import abort, make_response, redirect, render_template, request


@coin.before_first_request
def before_first_request():

    pass


@coin.before_request
def before_request():

    pass


@coin.after_request
def after_request():

    pass


@coin.teardown_request
def teardown_request():

    pass
