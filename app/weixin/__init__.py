# -*- coding: utf-8 -*-

"""

    coin.app.weixin
    ~~~~~~~~~~~~~~~

    stamaimer 08/23/16

"""

import sys
import time
import hashlib
import xmltodict
from lxml.etree import CDATA, Element, SubElement, tostring
from flask import Blueprint, current_app, g, request


weixin = Blueprint("weixin", __name__)


@weixin.before_request
def before_request():

    if request.endpoint != "weixin.get_access_token":

        g.access_token = current_app.test_client().get("/access_token").data


@weixin.route('/', methods=["GET"])
def verify():

    try:

        signature = request.args.get("signature")
        timestamp = request.args.get("timestamp")
        echostr   = request.args.get("echostr")
        nonce     = request.args.get("nonce")

        tmp_arr = [current_app.config["WEIXIN_TOKEN"], timestamp, nonce]

        tmp_str = ''.join(sorted(tmp_arr))

        tmp_str = hashlib.sha1(tmp_str).hexdigest()

        if tmp_str == signature:

            return echostr

        else:

            return '', 204

    except:

        current_app.logger.error(sys.exc_info())



