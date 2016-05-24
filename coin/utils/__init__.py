# -*- coding: utf-8 -*-

"""
    coin.utils
    ~~~~~~~~~~


"""

from coin import coin

from coin.models import db

import pymysql

import sys


def create_db():

    try:

        connection = pymysql.connect(host=coin.config["DB_HOST"], user=coin.config["DB_USER"], passwd=coin.config["DB_PSWD"])

        cursor = connection.cursor()

        cursor.execute("create database if not exists %s character set utf8 collate utf8_general_ci" % coin.config["DB_NAME"])

        coin.logger.info("database %s created" % coin.config["DB_NAME"])

    except:

        coin.logger.error(sys.exc_info()[1][1])

    finally:

        cursor.close()

        connection.close()


from coin.models.role import Role
from coin.models.user import User


def init_db():

    if coin.debug:

        coin.logger.info(coin.config["SQLALCHEMY_DATABASE_URI"])

        db.drop_all()

    db.create_all()

    admin_role = Role("admin")
    guest_role = Role("guest")

    db.session.add(admin_role)
    db.session.add(guest_role)

    admin_user = User("admin@example.com", "admin", True, [admin_role])

    guest_user = User("guest@example.com", "guest", True, [guest_role])

    db.session.add(admin_user)

    db.session.add(guest_user)
