#!/usr/bin/env bash
# start.sh

vagrant up

export APP_CONFIG_FILE=../config/development.py

# virtualenv venv

source ./venv/bin/activate

# pip install --upgrade pip

# pip install -r requirements.txt

python initial.py

gunicorn -w 30 -k gevent coin:coin -p coin.pid