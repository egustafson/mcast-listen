#!/usr/bin/env python3

import argparse
import ipaddress
import socket
import struct

DEFAULT_LISTEN_ADDR = '239.192.74.66'  ## collectd default IPv4 group
DEFAULT_LISTEN_PORT = 25826            ## collectd default port

DEFAULT_FWD_ADDR = '127.0.0.1'
DEFAULT_FWD_PORT = DEFAULT_LISTEN_PORT

def parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument("-l", "--laddr", type=str, default=DEFAULT_LISTEN_ADDR)
    parser.add_argument("-p", "--port", type=int, default=DEFAULT_LISTEN_PORT)
    parser.add_argument("-f", "--fwd", type=str, default=DEFAULT_FWD_ADDR)
    parser.add_argument("-fport", type=int, default=DEFAULT_FWD_PORT)
    return parser.parse_args()

if __name__ == '__main__':

    args = parse_args()
    l_addr = args.laddr
    l_port = args.port
    f_addr = args.fwd
    f_port = args.fport

    l_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    l_ip = ipaddress.ip_address(l_addr)
    if l_ip.is_multicast:
        print("listener is multicast.")
        l_sock.bind((l_addr, l_port))
        group = socket.inet_aton(l_addr)
        mreq = struct.pack('4sL', group, socket.INADDR_ANY)
        l_sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)
    else:
        l_sock.bind(('', l_port))  # listen for all traffic on the port

    f_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    print("forwarding: [{}:{}] -> [{}:{}]".format(l_addr, l_port, f_addr, f_port))

    dest = (f_addr, f_port)
    while True:
        data, addr = l_sock.recvfrom(10240) # network mtu up to 9k
        f_sock.sendto(data, dest)
