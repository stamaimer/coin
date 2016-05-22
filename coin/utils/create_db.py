# -*- coding: utf-8 -*-

import traceback

import pymysql

from coin.utils import coin


def create_db():

    try:

        connection = pymysql.connect(host=coin.config["DB_HOST"],
                                     user=coin.config["DB_USER"],
                                     passwd=coin.config["DB_PSWD"])

        cursor = connection.cursor()

        cursor.execute("create database if not exists %s character set utf8 collate utf8_general_ci" % coin.config["DB_NAME"])

        print "database %s created" % coin.config["DB_NAME"]

    except:

        traceback.print_exc()

    finally:

        cursor.close()

        connection.close()
