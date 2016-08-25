# -*- coding: utf-8 -*-

"""

    coin.app.api
    ~~~~~~~~~~~~

    stamaimer 08/19/16

"""

from flask import Blueprint

api = Blueprint("api", __name__)

import exam
import score
import student
import user

