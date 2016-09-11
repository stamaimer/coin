# -*- coding: utf-8 -*-

"""

    coin.app.main
    ~~~~~~~~~~~~~

    stamaimer 08/14/16

"""

from datetime import datetime
from flask import Blueprint, current_app, send_from_directory,make_response
from flask import abort, make_response, redirect, render_template, request
from flask_security import login_required
from flask_sqlalchemy import get_debug_queries
from app.model.pip_user import Pip_user
import hashlib, json, time

main = Blueprint("main", __name__)


@main.errorhandler(404)
def page_not_found(e):
    return render_template("404.html", error=''.join(e.description.args)), 404


@main.before_app_first_request
def before_app_first_request():
    pass


@main.before_app_request
def before_app_request():
    # if request.endpoint != 'main.profile' or request.endpoint != 'main.cv' or request.endpoint != 'main.news' or request.endpoint != 'main.podcast' or request.endpoint != 'main.pip' or request.endpoint != 'main.portfolio':

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
# @login_required
def index():
    return render_template("welcome.html")


@main.route('/welcome')
# @login_required
def welcome():
    return render_template("index.html")


@main.route('/signin')
# @login_required
def signin():
    return render_template("login.html")


@main.route('/nomination')
# @login_required
def nomination():
    return render_template("nomination.html")


@main.route('/access')
# @login_required
def access():
    return render_template("access.html")


@main.route('/auth')
# @login_required
def auth():
    try:
        user = Pip_user.query.filter_by(access_code=request.args.get('access-code')).first()

        resp = make_response(render_template("auth.html", user=user.to_json()))

        resp.set_cookie(key='ac', value=hashlib.md5(user.access_code).hexdigest(), expires=time.time() + 60 * 60)

        return resp
    except:

        return render_template("auth.html")


@main.route('/profile/<int:user_id>')
# @login_required
def profile(user_id):
    try:

        user = Pip_user.query.filter_by(id=user_id).first()

        if not user:
            raise Exception('Page not found')

        if hashlib.md5(user.email + user.password).hexdigest() == request.cookies.get('v'):

            return render_template("profile.html", user=user, owner=True)

        elif hashlib.md5(user.access_code).hexdigest() == request.cookies.get('ac'):

            return render_template("profile.html", user=user, owner=False)

        else:
            raise Exception('You have no access to view this profile')
    except Exception as e:

        abort(404,e)


@main.route('/invite')
# @login_required
def invite():
    return render_template("invite.html")


@main.route('/speaker')
# @login_required
def speaker():
    return render_template("speaker.html")


@main.route('/recruiter')
# @login_required
def recruiter():
    return render_template("recruiter.html")


@main.route('/profile/<int:user_id>/podcast')
# @login_required
def podcast(user_id):
    try:

        user = Pip_user.query.filter_by(id=user_id).first()

        if not user:
            raise Exception('Page not found')

        # podcast = json.loads(user.podcast.content)
        #
        # audio = user.podcast.audio

        if hashlib.md5(user.email + user.password).hexdigest() == request.cookies.get('v'):

            return render_template("podcast.html", user=user, owner=True)

        else:

            return render_template("podcast.html", user=user, owner=False)

    except Exception as e:

        abort(404)


@main.route('/profile/<int:user_id>/cv')
# @login_required
def cv(user_id):
    try:

        user = Pip_user.query.filter_by(id=user_id).first()

        if not user:
            raise Exception('Page not found')

        cv = json.loads(user.cv.content)

        if hashlib.md5(user.email + user.password).hexdigest() == request.cookies.get('v'):

            return render_template("cv.html", user=user, cv=cv, owner=True)

        else:

            return render_template("cv.html", user=user, cv=cv, owner=False)

    except Exception as e:

        abort(404)


@main.route('/profile/<int:user_id>/news')
# @login_required
def news(user_id):
    try:

        user = Pip_user.query.filter_by(id=user_id).first()

        if not user:
            raise Exception('Page not found')

        news = json.loads(user.news.content)

        if hashlib.md5(user.email + user.password).hexdigest() == request.cookies.get('v'):

            return render_template("news.html", user=user, news=news, owner=True)

        else:

            return render_template("news.html", user=user, news=news, owner=False)

    except Exception as e:

        abort(404)


@main.route('/portfolio')
# @login_required
def portfolio():
    return render_template("portfolio.html", owner=request.args.get('owner'), user=request.args.get('user'))


@main.route('/profile/<int:user_id>/pip')
# @login_required
def pip(user_id):
    try:

        user = Pip_user.query.filter_by(id=user_id).first()

        if not user:
            raise Exception('Page not found')

        pip = json.loads(user.pip_block.content)

        if hashlib.md5(user.email + user.password).hexdigest() == request.cookies.get('v'):

            return render_template("pip.html", user=user, pip=pip, owner=True)

        else:

            return render_template("pip.html", user=user, pip=pip, owner=False)

    except Exception as e:

        abort(404)


@main.route('/v/<filename>')
def get_file(filename):
    return send_from_directory("static/video/", filename)

#
# @main.app_errorhandler(404)
# def page_not_found():
#
#     pass
