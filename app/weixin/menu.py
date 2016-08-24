# -*- coding: utf-8 -*-

"""

    coin.app.weixin.menu
    ~~~~~~~~~~~~~~~~~~~~

    stamaimer 08/23/16

"""

from flask import current_app
from . import weixin


@weixin.route("/menu", methods=["POST"])
def create_menu():

    endpoint = current_app.config["WEIXIN_ENDPOINT"] + "/cgi-bin/menu/create?access_token=" + g.access_token


@weixin.route("/menu", methods=["GET"])
def select_menu():

    pass