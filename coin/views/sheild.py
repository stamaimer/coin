# -*- coding: utf-8 -*-

from . import *
from itsdangerous import URLSafeTimedSerializer

ts = URLSafeTimedSerializer(coin.config["SECRET_KEY"])


