#!/usr/bin/env python
import socket
import struct
import binascii
def print_mac(h):
    s=""
    for i in range(0,12,2):
        s+=h[i:i+2]+":"
    s=s[:-1]
    return s
def eth_unpack(pkt):
    a = pkt[0][0:14]
    header = struct.unpack("!6s6s2s", a)
    print print_mac(binascii.hexlify(header[0]))+" => this is dst address"
    print print_mac(binascii.hexlify(header[1]))+" => this is src address"
    print binascii.hexlify(header[2])+" => this is type"

def ip_unpack(pkt):
    a = pkt[0][14:34]
    header = struct.unpack("!12s4s4s", a)
    print socket.inet_ntoa(header[1])+"=> dst ip"
    print socket.inet_ntoa(header[2])+"=> src ip"

a = socket.socket(socket.PF_PACKET,socket.SOCK_RAW, socket.htons(0x0800))
while True:
    pkt = a.recvfrom(2048)
    print "="*25
    eth_unpack(pkt)
    ip_unpack(pkt)
