# -*- coding: utf-8 -*-

"""
    coin.config
    ~~~~~~~~~~~

    stamaimer 08/15/16

"""


class Config(object):

    # configuration of flask

    HOST = "0.0.0.0"

    PORT = 2333

    DEBUG = 1

    TESTING = 0

    # configuration of flask-debugtoolbar

    DEBUG_TB_PROFILER_ENABLED = 1

    DEBUG_TB_INTERCEPT_REDIRECTS = 0

    DEBUG_TB_TEMPLATE_EDITOR_ENABLED = 1

    # configuration of flask-mail

    MAIL_SERVER = "smtp.qq.com"

    MAIL_PORT = "465"

    MAIL_USE_TLS = 0

    MAIL_USE_SSL = 1

    MAIL_DEFAULT_SENDER = "2518930466@qq.com"
    
    # configuration of flask-sqlalchemy

    SQLALCHEMY_RECORD_QUERIES = True

    SQLALCHEMY_TRACK_MODIFICATIONS = True

    SQLALCHEMY_COMMIT_ON_TEARDOWN = True

    # configuration of flask-security

    SECURITY_CONFIRMABLE = 1

    SECURITY_REGISTERABLE = True

    SECURITY_RECOVERABLE = 1

    SECURITY_TRACKABLE = 1

    SECURITY_PASSWORD_HASH = "bcrypt"

    SECURITY_SEND_REGISTER_EMAIL = 1

    SECURITY_EMAIL_SENDER = "2518930466@qq.com"

    @staticmethod
    def init_app(app):

        pass


from development import DevelopmentConfig
from production import ProductionConfig
from staging import StagingConfig

config = {
    "default": DevelopmentConfig,
    "development": DevelopmentConfig,
    "production": ProductionConfig,
    "staging": StagingConfig
}