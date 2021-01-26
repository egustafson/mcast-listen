FROM python:3.8

WORKDIR /app

copy mcast_listen.py .

cmd [ "python", "./mcast_listen.py" ]
