#!/usr/bin/env bash
# start.sh

export APP_CONFIG_FILE=../config/development.py

# virtualenv venv

source ./venv/bin/activate

# pip install --upgrade pip

# pip install -r requirements.txt

gunicorn -w 10 -k sync coin:coin -p coin.pid ¬