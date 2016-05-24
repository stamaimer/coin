# -*- coding: utf-8 -*-

"""
    coin.api
    ~~~~~~~~~~


"""

from flask.ext.restless import APIManager

from coin import coin

from coin.models import db

from coin.models.user import User

api = APIManager(coin, flask_sqlalchemy_db=db)

api.create_api(User, methods=["GET", "POST", "DELETE"])

