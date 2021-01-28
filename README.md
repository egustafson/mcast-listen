# UDP Forwarder w/ Multicast

This package provides a UDP forwarder that will subscribe to a
multicast group if told to listen on a multicast address.  UDP
payloads are copied 1:1 to the destination.

Also included is 'udp_listen' which will listen and properly subscribe
to the multicast group when presented a multicast address to listen
to.

*collectd* forwarder:  the udpfwd.py can be used to forward collectd
(i.e. udp) datagrams from a multicast address to a unicast address.
This may be useful if the end destination is inside a Docker container
where that is not using host networking.  This was the use-case for
the code.
