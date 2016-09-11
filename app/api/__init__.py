# -*- coding: utf-8 -*-

"""

    coin.app.api
    ~~~~~~~~~~~~

    stamaimer 08/19/16

"""

from flask import Blueprint, request, Response, render_template
from app.model.pip_user import Pip_user
import time, json, hashlib

api = Blueprint("api", __name__)


@api.route('/')
def index():
    return "failed"


@api.route('/login', methods=['POST'])
def login():
    email = request.form['email']

    password = request.form['password']

    try:
        user = Pip_user.query.filter_by(email=email).first()

        if not user:
            raise Exception("Email not exist. ", email)

        if not user.password == password:
            raise Exception("Password not correct. ", email)

        res = Response()

        res.set_cookie(key='v', value=hashlib.md5(user.email + user.password).hexdigest(),
                       expires=time.time() + 60 * 60)

        data = {}

        data['status'] = "success"

        data['user'] = user.to_json()

        res.data = json.dumps(data)

        return res

    except Exception as e:

        res = Response()

        data = {}

        data['status'] = "fail"

        data['reason'] = ''.join(e.args)

        res.data = json.dumps(data)

        return res


        # if email == 'example1@pip.com' and password == 'example1':
        #
        #     return "?owner=true&user=1"
        #
        # if email == 'example2@pip.com' and password == 'example2':
        #
        #     return "?owner=true&user=2"
        #
        # return "failed"
