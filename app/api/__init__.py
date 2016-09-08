# -*- coding: utf-8 -*-

"""

    coin.app.api
    ~~~~~~~~~~~~

    stamaimer 08/19/16

"""

from flask import Blueprint, request, render_template

api = Blueprint("api", __name__)


@api.route('/')
def index():

    return "failed"


@api.route('/login', methods=['POST'])
def login():
    email = request.form['email']

    password = request.form['password']

    if email == 'example1@pip.com' and password == 'example1':

        return "?owner=true&user=1"

    if email == 'example2@pip.com' and password == 'example2':

        return "?owner=true&user=2"

    return "failed"
