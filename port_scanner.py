#!/usr/bin/env python
import sys
from scapy.all import *
import threading
from Queue import Queue
def pinging(ip):
    a = IP(dst=ip)/ICMP()
    b = sr1(a,timeout=5,verbose=0)
    if b:
        print "Initiating PortScan....."
    else :
        print "Host is down or is'nt reachable"
        sys.exit()
    
def portscan(q,ip):
    i = q.get()
    a = IP(dst=ip)/TCP(dport=i,flags="S")
    b = sr1(a,timeout=1,verbose=0)
    if "SA" in str(b.getlayer(TCP).flags):
        print "%d => is open" %i
        a = IP(dst=ip)/TCP(dport=i,flags="R")
        b = send(a,verbose=0)
    q.task_done()


if sys.argv[1]:
    ip = sys.argv[1]
    print "Pinging ip"
    q = Queue()
    for i in range(1,65536):
        q.put(i)
    pinging(ip)
    while True:
        try:
            for i in range(10):
                worker = threading.Thread(target=portscan, args=(q,ip))
                worker.setDaemon(True)
                worker.start()
        except :
            print "Scanning done"
            sys.exit()
    q.join()
