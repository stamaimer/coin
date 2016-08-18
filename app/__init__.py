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


debug_toolbar = DebugToolbarExtension()

bootstrap = Bootstrap()

moment = Moment()


def create_app(config_name):

    app = Flask(__name__, instance_relative_config=1)

    app.config.from_object(config_name)

    app.config.from_pyfile("config.py")

    debug_toolbar.init_app(app)

    bootstrap.init_app(app)

    moment.init_app(app)

    from admin import admin

    admin.init_app(app)

    from mail import mail

    mail.init_app(app)

    from model import db

    db.init_app(app)

    from security import security

    security.init_app(app)

    return app
