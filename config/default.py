import os

DEBUG = True

UPLOAD_DIR = os.getcwd() + "/coin/static/upload"

MAX_CONTENT_LENGTH = 4 * 1024 * 1024

SQLALCHEMY_TRACK_MODIFICATIONS = True
