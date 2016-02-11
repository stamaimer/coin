from flask import Flask
from coin import views

coin = Flask(__name__, instance_relative_config=True)

coin.config.from_object('config.default')

coin.config.from_pyfile('config.py')

coin.config.from_envvar('APP_CONFIG_FILE')
