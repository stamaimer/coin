#!/usr/bin/env bash
# start.sh

gunicorn -w 1 -k gevent coin:coin -p coin.pid -b 127.0.0.1:6666
