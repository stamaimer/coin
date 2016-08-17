# -*- coding: utf-8 -*-

"""
    config
    ~~~~~~

    stamaimer 08/15/16

"""


class Config(object):

    # configuration of flask

    DEBUG = 1

    TESTING = 1

    # configuration of flask-debugtoolbar

    DEBUG_TB_PROFILER_ENABLED = 1

    DEBUG_TB_TEMPLATE_EDITOR_ENABLED = 1

    # configuration of flask-sqlalchemy

    SQLALCHEMY_TRACK_MODIFICATIONS = True
