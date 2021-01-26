#!/usr/bin/env python3

import socket
import struct
import sys

multicast_group = '239.192.74.66'  ## collectd default IPv4 group
server_address = ('', 25826)       ## collectd default port

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.bind(server_address)

group = socket.inet_aton(multicast_group)
mreq = struct.pack('4sL', group, socket.INADDR_ANY)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

sys.stderr.write("Listening for multicast messages...\n")
while True:
    data, address = sock.recvfrom(10240) # network MTU is 9k
    sys.stderr.write("recv {} bytes from {}\n".format(len(data), address))
