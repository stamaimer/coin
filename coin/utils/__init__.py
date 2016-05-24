# -*- coding: utf-8 -*-

"""
    coin.utils
    ~~~~~~~~~~


"""

from coin import coin

from coin.models import db
from coin.models.role import Role
from coin.models.user import User

import pymysql

import sys


def create_user(password):

    try:

        connection = pymysql.connect(host=coin.config["DB_HOST"], user="root", passwd=password)

        cursor = connection.cursor()

        cursor.execute("grant all on %s.* to '%s' identified by '%s'" %
                       (coin.config["DB_NAME"],
                        coin.config["DB_USER"],
                        coin.config["DB_PSWD"]))

    except:

        coin.logger.info(cursor._last_executed)

        coin.logger.error(sys.exc_info()[1][1])

    finally:

        cursor.close()

        connection.close()


def create_database(password):

    try:

        connection = pymysql.connect(host=coin.config["DB_HOST"], user="root", passwd=password)

        cursor = connection.cursor()

        cursor.execute("create database if not exists %s character set utf8 collate utf8_general_ci" % coin.config["DB_NAME"])

    except:

        coin.logger.info(cursor._last_executed)

        coin.logger.error(sys.exc_info()[1][1])

    finally:

        cursor.close()

        connection.close()


def resets_database():

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
