# -*- coding: utf-8 -*-

"""

    coin.admin

    stamaimer 08/15/16

"""

from flask import current_app
from flask_admin import Admin

admin = Admin(name="Coin Dashboard", template_mode="bootstrap3")
