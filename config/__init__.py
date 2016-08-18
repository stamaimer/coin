# -*- coding: utf-8 -*-

"""
    config
    ~~~~~~

    stamaimer 08/15/16

"""


class Config(object):

    # configuration of flask

    HOST = "0.0.0.0"

    PORT = 5000

    DEBUG = 1

    TESTING = 1

    # configuration of flask-debugtoolbar

    DEBUG_TB_PROFILER_ENABLED = 1

    DEBUG_TB_INTERCEPT_REDIRECTS = 0

    DEBUG_TB_TEMPLATE_EDITOR_ENABLED = 1

    # configuration of flask-mail

    MAIL_SERVER = "smtp.gmail.com"

    MAIL_PORT = "587"

    MAIL_USE_TLS = 0

    MAIL_USE_SSL = 0

    MAIL_DEFAULT_SENDER = "noreply@coin.com"
    
    # configuration of flask-sqlalchemy

    SQLALCHEMY_TRACK_MODIFICATIONS = True

    # configuration of flask-security

    SECURITY_CONFIRMABLE = 0

    SECURITY_REGISTERABLE = True

    SECURITY_RECOVERABLE = 1

    SECURITY_TRACKABLE = 1

    SECURITY_PASSWORD_HASH = "bcrypt"

