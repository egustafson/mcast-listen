#!/bin/sh

docker run -it --rm \
       --name="mcastlisten" \
       --net="localnet" \
       -p 25826:25826/udp \
       mcastlisten

#       --net="host" \
