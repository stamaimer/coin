# -*- coding: utf-8 -*-

"""

    coin.run
    ~~~~~~~~

    stamaimer 08/18/16

"""

from app import create_app

app = create_app("config.development.DevelopmentConfig")

app.run(host=app.config["HOST"], port=app.config["PORT"], threaded=1)
