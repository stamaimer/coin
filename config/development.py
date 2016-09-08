# -*- coding: utf-8 -*-

"""

    coin.config.development
    ~~~~~~~~~~~~~~~~~~~~~~~

    stamaimer 08/15/16

"""

from config import Config


class DevelopmentConfig(Config):

    # configuration of flask-sqlalchemy

    SQLALCHEMY_TRACK_MODIFICATIONS = True
