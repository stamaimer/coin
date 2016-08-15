# -*- coding: utf-8 -*-

"""

    coin
    ~~~~

    stamaimer 08/14/16

"""


from flask import Flask
from flask_script import Manager
from flask_bootstrap import Bootstrap
from flask_moment import Moment


coin = Flask(__name__)

manager = Manager(coin)

bootstrap = Bootstrap(coin)

moment = Moment(coin)
