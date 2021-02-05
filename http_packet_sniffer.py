#!/usr/bin/env python

import scapy.all as scapy

def working(a):
    print "="*25
    try:
        if "HTTP" in a.load:
            b = str(a.load).split("\r\n")
            for i in range(len(b)):
                print b[i]

    except:
        pass

            

a=scapy.sniff(iface="eth0", prn=working, filter="tcp port 80")
