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

        g.access_token = current_app.test_client().get("/weixin/access_token").data


@weixin.route("/", methods=["GET"])
def verify():

    try:

        signature = request.args.get("signature")
        timestamp = request.args.get("timestamp")
        echostr   = request.args.get("echostr")
        nonce     = request.args.get("nonce")

        tmp_arr = [current_app.config["WEIXIN_TOKEN"], timestamp, nonce]

        tmp_str = ''.join(sorted(tmp_arr))

        tmp_str = hashlib.sha1(tmp_str).hexdigest()

    except:

        current_app.logger.error(sys.exc_info())

    finally:

        if tmp_str == signature:

            return echostr

        else:

            return '', 204


@weixin.route('/', methods=["POST"])
def message():

    try:

        data = xmltodict.parse(request.data)["xml"]

        xml = Element("xml")

        ToUserName = SubElement(xml, "ToUserName")

        ToUserName.text = CDATA(data["FromUserName"])

        FromUserName = SubElement(xml, "FromUserName")

        FromUserName.text = CDATA(data["ToUserName"])

        CreateTime = SubElement(xml, "CreateTime")

        CreateTime.text = str(int(time.time()))

        MsgType = SubElement(xml, "MsgType")

        MsgType.text = CDATA("text")

        Content = SubElement(xml, "Content")

        if data["MsgType"] == "event" and data["Event"] == "subscribe":

            Content.text = CDATA(u"感谢关注")

        elif data["MsgType"] == "text" and data["Content"] == u"最新成绩":

            Content.text = CDATA(u"最新成绩")

        elif data["MsgType"] == "text" and data["Content"] == u"所有成绩":

            Content.text = CDATA(u"历史成绩")

        else:

            Content.text = CDATA(u"再说一遍")

    except:

        current_app.logger.error(sys.exc_info())

    finally:

        current_app.logger.debug(tostring(xml, encoding="utf-8", pretty_print=1))

        return tostring(xml, encoding="utf-8")


import menu
import access_token