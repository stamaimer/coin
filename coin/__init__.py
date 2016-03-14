# -*- coding: utf-8 -*-
from flask import Flask

coin = Flask(__name__, instance_relative_config=True)  # __name__

# load the default configuration
coin.config.from_object('config.default')

# load the configuration from the instance folder
coin.config.from_pyfile('config.py')

# load the file specified by the APP_CONFIG_FILE environment variable
# variables defined here will override those in the default configuration
coin.config.from_envvar('APP_CONFIG_FILE')

from logger import init_logger

init_logger()

from models import init_db

init_db()

import security

import admin

import views

