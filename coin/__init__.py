# -*- coding: utf-8 -*-

from flask import Flask
from flask.ext.admin import Admin
from flask_admin import helpers as admin_helpers
from flask.ext.cache import Cache
from flask.ext.bcrypt import Bcrypt
from flask.ext.security import Security, SQLAlchemyUserDatastore, current_user, login_required
from flask.ext.sqlalchemy import SQLAlchemy

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

admin = Admin(coin, name="Coin Dashboard", template_mode="bootstrap3")

cache = Cache(coin)

db = SQLAlchemy(coin)

bcrypt = Bcrypt(coin)

from models import init_db, Role, User, Task

init_db()

user_datastore = SQLAlchemyUserDatastore(db, User, Role)

security = Security(coin, user_datastore)

user_datastore.create_user(email="stamaimer@gmail.com", password="stamaimer")

db.session.commit()


@security.context_processor
def security_context_processor():

    return dict(
        admin_base_template=admin.base_template,
        admin_view=admin.index_view,
        h=admin_helpers,
    )

import admin

from views  import *
