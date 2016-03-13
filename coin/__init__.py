# -*- coding: utf-8 -*-

from flask import Flask
from flask.ext.cache import Cache
from flask.ext.bcrypt import Bcrypt

coin = Flask(__name__, instance_relative_config=True)  # __name__

# load the default configuration
coin.config.from_object('config.default')

# load the configuration from the instance folder
coin.config.from_pyfile('config.py')

# load the file specified by the APP_CONFIG_FILE environment variable
# variables defined here will override those in the default configuration
coin.config.from_envvar('APP_CONFIG_FILE')


def init_logger():

    if not coin.debug:

        from logging import Formatter

        from logging import FileHandler

        file_handler = FileHandler("./log/coin.log")

        file_handler.setFormatter(Formatter("%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]"))

        coin.logger.addHandler(file_handler)


cache = Cache(coin)

bcrypt = Bcrypt(coin)

from models import init_db

init_db()

import admin

import security

import views

