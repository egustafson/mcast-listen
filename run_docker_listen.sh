#!/bin/sh

docker run -it --rm \
       --name="udplisten" \
       --net="localnet" \
       -p 10000:10000/udp \
       udplisten python ./udp_listen.py -l 0.0.0.0 -p 10000
