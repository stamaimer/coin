# -*- coding: utf-8 -*-

from itsdangerous import URLSafeTimedSerializer

from coin import coin

ts = URLSafeTimedSerializer(coin.config["SECRET_KEY"])


