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
from flask_redis import FlaskRedis
from raven.contrib.flask import Sentry


debug_toolbar = DebugToolbarExtension()

bootstrap = Bootstrap()

moment = Moment()

sentry = Sentry()

redis = FlaskRedis()


def create_app(config_name):

    app = Flask(__name__, instance_relative_config=1)

    app.config.from_object(config_name)

    app.config.from_pyfile("config.py")

    debug_toolbar.init_app(app)

    bootstrap.init_app(app)

    moment.init_app(app)

    redis.init_app(app)

    if not app.config["DEBUG"]: sentry.init_app(app)

    from admin import admin

    admin.init_app(app)

    from mail import mail

    mail.init_app(app)

    from model import db

    db.init_app(app)

    from security import security

    security.init_app(app)

    from weixin import weixin as weixin_blueprint

    from main import main as main_blueprint

    from api import api as api_blueprint

    app.register_blueprint(main_blueprint)

    app.register_blueprint(weixin_blueprint, url_prefix="/weixin")

    app.register_blueprint(api_blueprint, url_prefix="/api")

    return app
