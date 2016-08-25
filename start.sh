#!/usr/bin/env bash
# start.sh

virtualenv venv

source venv/bin/activate

pip install --upgrade pip

pip install -r requirements.txt -i http://pypi.douban.com/simple/ --trusted-host=pypi.douban.com