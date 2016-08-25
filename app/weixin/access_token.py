# -*- coding: utf-8 -*-

"""

    coin.app.weixin.access_token
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    stamaimer 08/23/16

"""

import sys
import requests
from flask import current_app, request
from app import redis
from . import weixin


@weixin.route("/access_token", methods=["GET"])
def get_access_token():

    try:

        expires_in = redis.ttl("access_token")

        if expires_in > 60:

            access_token = redis.get("access_token")

        else:

            get_access_token_from_weixin()

            access_token = redis.get("access_token")

    except:

        current_app.logger.error(sys.exc_info())

    finally:

        return access_token


def get_access_token_from_weixin():

    endpoint = current_app.config["WEIXIN_ENDPOINT"] + "/cgi-bin/token"

    payload = dict()

    payload["grant_type"] = "client_credential"

    payload["appid"] = current_app.config["WEIXIN_APP_ID"]

    payload["secret"] = current_app.config["WEIXIN_APP_SECRET"]

    try:

        response = requests.get(endpoint, payload)

        if response.status_code == requests.codes.ok:

            data = response.json()

            if "access_token" in data:

                redis.set("access_token", data["access_token"])

                redis.expire("access_token", data["expires_in"])

            else:

                current_app.logger.error(data)

        else:

            current_app.logger.error(response.status_code + ": " + response.reason)

    except:

        current_app.logger.error(sys.exc_info())


@weixin.route("/web_access_token", methods=["GET"])
def get_web_access_token():

    try:

        expires_in = redis.ttl("web_access_token")

        if expires_in > 60:

            web_access_token = redis.get("web_access_token")

        else:

            get_web_access_token_from_weixin(request.args.get("code"))

            web_access_token = redis.get("web_access_token")

    except:

        current_app.logger.error(sys.exc_info())

    finally:

        return web_access_token


def get_web_access_token_from_weixin(code):

    endpoint = current_app.config["WEIXIN_ENDPOINT"] + "/sns/oauth2/access_token"

    payload = dict()

    payload["code"] = code

    payload["appid"] = current_app.config["WEIXIN_APP_ID"]
