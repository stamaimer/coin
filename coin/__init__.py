# -*- coding: utf-8 -*-
"""
    coin
    ~~~~


"""

__version__ = "0.1.dev0"

from flask import Flask
from flask.ext.babelex import Babel
from flask.ext.debugtoolbar import DebugToolbarExtension

from werkzeug.contrib.fixers import ProxyFix

coin = Flask(__name__, instance_relative_config=True)  # __name__

coin.wsgi_app = ProxyFix(coin.wsgi_app)

# load the default configuration
coin.config.from_object('config.default')

# load the configuration from the instance folder
coin.config.from_pyfile('config.py')

# load the file specified by the APP_CONFIG_FILE environment variable
# variables defined here will override those in the default configuration
coin.config.from_envvar('APP_CONFIG_FILE', silent=True)

debugger = DebugToolbarExtension(coin)

babel = Babel(coin)

import admin

import security

import views

import mail

