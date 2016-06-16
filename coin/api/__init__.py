# -*- coding: utf-8 -*-

"""
    coin.api
    ~~~~~~~~~~


"""

from flask.ext.restless import APIManager

from coin import coin

from coin.models import db


from coin.models.user import User

api_manager = APIManager(coin, flask_sqlalchemy_db=db)

api_manager.create_api(User, methods=["GET", "POST", "DELETE"])

