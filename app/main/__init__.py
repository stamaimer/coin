# -*- coding: utf-8 -*-

"""

    coin.app.main
    ~~~~~~~~~~~~~

    stamaimer 08/14/16

"""

from datetime import datetime
from flask import Blueprint, current_app, url_for
from flask import abort, make_response, redirect, render_template, request
from flask_security import login_required
from flask_sqlalchemy import get_debug_queries


main = Blueprint("main", __name__)


@main.before_app_first_request
def before_app_first_request():

    pass


@main.before_app_request
def before_app_request():

    pass


@main.after_app_request
def after_app_request(response):

    for query in get_debug_queries():

        current_app.logger.debug(query)

    return response


@main.teardown_app_request
def teardown_app_request(response):

    return response


@main.route('/')
def index():

    return 'hhh'

    return render_template("index.html", current_time=datetime.utcnow())


# @main.app_errorhandler(404)
# def page_not_found(response):
#
#     pass


@main.route("/input", methods=["GET"])
def _input():

    return render_template('input.html')


@main.route("/list", methods=["GET"])
def _list():

    exams = current_app.test_client().get(url_for('api.get_exam', _external=True))

    return render_template('list.html', exams=exams.data)


@main.route("/students", methods=["GET"])
def students():

    return render_template('students.html')

