#!/usr/bin/env bash
# start.sh

# vagrant up

export APP_CONFIG_FILE=../config/development.py

# virtualenv venv

source ./venv/bin/activate

# pip install --upgrade pip

# pip install -r requirements.txt

python initial.py $1

gunicorn -w 10 -k gevent coin:coin -p coin.pid