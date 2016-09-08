# -*- coding: utf-8 -*-

"""

    coin.app.main
    ~~~~~~~~~~~~~

    stamaimer 08/14/16

"""

from datetime import datetime
from flask import Blueprint, current_app, send_from_directory
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

    # if request.path == "/static/video/test.mp4":
    #
    # 	response.headers['Content-Type'] = "video/mp4"
    #
    # 	response.headers['Accept-Ranges'] = "bytes0-"

    return response


@main.teardown_app_request
def teardown_app_request(response):
    return response


@main.route('/')
@login_required
def index():
    return render_template("welcome.html")


@main.route('/welcome')
@login_required
def welcome():
    return render_template("index.html")


@main.route('/signin')
@login_required
def signin():
    return render_template("login.html")


@main.route('/nomination')
@login_required
def nomination():
    return render_template("nomination.html")


@main.route('/access')
@login_required
def access():
    return render_template("access.html")


@main.route('/auth')
@login_required
def auth():
    return render_template("auth.html", owner=request.args.get('owner'), user=request.args.get('user'))


@main.route('/profile')
@login_required
def profile():

    return render_template("profile.html", owner=request.args.get('owner'), user=request.args.get('user'))


@main.route('/invite')
@login_required
def invite():
    return render_template("invite.html")


@main.route('/speaker')
@login_required
def speaker():
    return render_template("speaker.html")


@main.route('/recruiter')
@login_required
def recruiter():
    return render_template("recruiter.html")


@main.route('/podcast')
@login_required
def podcast():
    return render_template("podcast.html", owner=request.args.get('owner'), user=request.args.get('user'))


@main.route('/cv')
@login_required
def cv():
    return render_template("cv.html", owner=request.args.get('owner'), user=request.args.get('user'))


@main.route('/news')
@login_required
def news():
    return render_template("news.html", owner=request.args.get('owner'), user=request.args.get('user'))


@main.route('/portfolio')
@login_required
def portfolio():
    return render_template("portfolio.html", owner=request.args.get('owner'), user=request.args.get('user'))


@main.route('/pip')
@login_required
def pip():
    return render_template("pip.html", owner=request.args.get('owner'), user=request.args.get('user'))


@main.route('/v/<filename>')
def get_file(filename):
    return send_from_directory("static/video/", filename)

#
# @main.app_errorhandler(404)
# def page_not_found():
#
#     pass
