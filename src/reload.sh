#!/bin/sh



PROCS=$(ps aux | grep manage.py | grep python | awk '{print $2}')

if [ -n "$PROCS" ]; then
	kill $PROCS
fi

python ./manage.py runfcgi host=127.0.0.1 port=8080
