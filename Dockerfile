FROM python:3.8

WORKDIR /app

copy udpfwd.py .

cmd [ "python", "./udpfwd.py" ]
