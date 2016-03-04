from flask import Flask
from flask.ext.cache import Cache
from flask.ext.bcrypt import Bcrypt
from flask.ext.sqlalchemy import SQLAlchemy

coin = Flask(__name__, instance_relative_config=True)  # __name__

# load the default configuration
coin.config.from_object('config.default')

# load the configuration from the instance folder
coin.config.from_pyfile('config.py')

# load the file specified by the APP_CONFIG_FILE environment variable
# variables defined here will override those in the default configuration
coin.config.from_envvar('APP_CONFIG_FILE')

coin.debug      = coin.config["DEBUG"]
coin.secret_key = coin.config["SECRET_KEY"]


if not coin.debug:

    import logging

    from logging import Formatter

    from logging import FileHandler

    file_handler = FileHandler("./log/coin.log")

    file_handler.setFormatter(Formatter("%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]"))

    coin.logger.addHandler(file_handler)

db = SQLAlchemy(coin)

bcrypt = Bcrypt(coin)

cache = Cache(coin)

import views
