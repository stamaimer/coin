import os

DEBUG = True

DEBUG_TB_PROFILER_ENABLED = True

DEBUG_TB_INTERCEPT_REDIRECTS = False

DEBUG_TB_TEMPLATE_EDITOR_ENABLED = True

HOST = "0.0.0.0"

PORT = 4096

UPLOAD_DIR = os.getcwd() + "/coin/static/upload"

MAX_CONTENT_LENGTH = 4 * 1024 * 1024

SQLALCHEMY_ECHO = True

SQLALCHEMY_TRACK_MODIFICATIONS = True

CACHE_TYPE = "simple"

SECURITY_TRACKABLE = True

SECURITY_CONFIRMABLE = False

SECURITY_REGISTERABLE = True


