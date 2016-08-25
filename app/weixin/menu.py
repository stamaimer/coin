# -*- coding: utf-8 -*-

"""

    coin.app.weixin.menu
    ~~~~~~~~~~~~~~~~~~~~

    stamaimer 08/23/16

"""

import sys
import json
import requests
from flask import current_app, g
from . import weixin


@weixin.route("/menu", methods=["POST"])
def create_menu():

    endpoint = current_app.config["WEIXIN_ENDPOINT"] + "/cgi-bin/menu/create?access_token=" + g.access_token

    button_list = list()

    button_current = dict()

    button_history = dict()

    button_current["type"] = "click"

    button_current["name"] = "最新成绩"

    button_current["key"] = "CURRENT"

    button_history["type"] = "click"

    button_history["name"] = "所有成绩"

    button_history["type"] = "HISTORY"

    button_list.extend([button_current, button_history])

    payload = dict()

    payload["button"] = button_list

    try:

        response = requests.post(endpoint, data=json.dumps(payload, ensure_ascii=0))

        if response.status_code == requests.codes.ok:

            current_app.logger.info(response.json())

        else:

            current_app.logger.error(response.status_code + ": " + response.reason)

    except:

        current_app.logger.error(sys.exc_info())

    finally:

        return '', 204


@weixin.route("/menu", methods=["GET"])
def select_menu():

    pass