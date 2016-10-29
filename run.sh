#!/bin/bash

port=1234
count=`netstat -ant | grep LISTEN | grep -c ":${port}\W"`

if [ $count -gt 0 ]; then
    echo "You're already running a server"
    exit 1
fi

while true; do
    python manage.py runserver 0.0.0.0:$port
    sleep 1
done
