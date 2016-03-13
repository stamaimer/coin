import os

DEBUG = True

HOST = "0.0.0.0"

PORT = 4096

UPLOAD_DIR = os.getcwd() + "/coin/static/upload"

MAX_CONTENT_LENGTH = 4 * 1024 * 1024

SQLALCHEMY_TRACK_MODIFICATIONS = True

CACHE_TYPE = "simple"

SECURITY_TRACKABLE = False

SECURITY_CONFIRMABLE = False


