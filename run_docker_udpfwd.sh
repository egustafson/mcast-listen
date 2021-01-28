#!/bin/sh

docker run -it --rm \
       --name="udpfwd" \
       --net="host" \
       udpfwd python ./udpfwd.py -f 10.3.4.89 -fport 10000

