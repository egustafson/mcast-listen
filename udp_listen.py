#!/usr/bin/env python3

import argparse
import ipaddress
import socket
import struct

DEFAULT_ADDR = '127.0.0.1'
DEFAULT_PORT = 25826

def parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument("-l", "--laddr", type=str, default=DEFAULT_ADDR)
    parser.add_argument("-p", "--port", type=int, default=DEFAULT_PORT)
    return parser.parse_args()


if __name__ == '__main__':

    args = parse_args()

    # multicast_group = '239.192.74.66'  ## collectd default IPv4 group
    # server_address = (multicast_group, 25826)       ## collectd default port

    l_addr = args.laddr
    l_port = args.port

    l_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    l_sock.bind((l_addr, l_port))
    l_ip = ipaddress.ip_address(l_addr)
    if l_ip.is_multicast:
        print("multicast listener")
        group = socket.inet_aton(l_addr)
        mreq = struct.pack('4sL', group, socket.INADDR_ANY)
        l_sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

    print("Listening:  {}:{}".format(args.laddr, args.port))
    while True:
        data, addr = l_sock.recvfrom(10240) # network MTU is 9k
        print("recv {} bytes from {}".format(len(data), addr))
