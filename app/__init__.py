# -*- coding: utf-8 -*-

"""

    coin.app
    ~~~~~~~~

    stamaimer 08/14/16

"""


from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from raven.contrib.flask import Sentry

debug_toolbar = DebugToolbarExtension()

bootstrap = Bootstrap()

moment = Moment()

sentry = Sentry()


def create_app(config_name):

    app = Flask(__name__, instance_relative_config=1)

    app.config.from_object(config_name)

    app.config.from_pyfile("config.py")

    debug_toolbar.init_app(app)

    bootstrap.init_app(app)

    moment.init_app(app)

    if not app.config["DEBUG"]: sentry.init_app(app)

    from admin import admin

    admin.init_app(app)

    from mail import mail

    mail.init_app(app)

    from model import db

    db.init_app(app)

    from security import security

    security.init_app(app)

    from view import view

    app.register_blueprint(view)

    return app
