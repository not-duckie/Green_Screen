"""
This script is little bit better than the dir_brute.py as this will recursively search through directories according to depth specified as input/
I have not yet implemented user-friendly input will do it in a while.
"""
#!/usr/bin/env python
import requests
import sys
from Queue import Queue
import threading

def making_queue(url,dic):
    q = Queue()
    f = open(dic,"rt")
    for i in f.readlines():
        q.put(i)
    while True:
        try:
            for i in range(10):
                worker = threading.Thread(target=spider,args=(url,q))
                worker.setDaemon(True)
                worker.start()
        except :
            print "Done"
            exit()
    q.join()


def recursive(a,d):
    dic = sys.argv[1]
    f = open(dic,"rt")
    url = a
    proxy = {"http":"http://127.0.0.1:8080"}
    if d:
        for i in f.readlines():
            a = url+"/"
            i=i.strip()
            a = a+i
            r = requests.get(a,proxies=proxy,allow_redirects=False)
            if str(r.status_code) in "301,302":
                print a.encode("utf-8") + "=> directory"
                d = d-1
                print "+"*25
                recursive(a,d)
            if str(r.status_code) in "200":
                print a.encode("utf-8")
    else:
        print "recusrion limit reached"

def spider(url,q):
    depth = 5
    proxy = {"http":"http://127.0.0.1:8080"}
    i = q.get()
    i = i.strip()
    a = url+i
    r = requests.get(a,proxies=proxy,allow_redirects=False)
    if str(r.status_code) in "301,302":
        print a+" => directory"
        recursive(a,depth)
    if str(r.status_code) in "200":
        print a
url = "https://www.hackthissite.org/"
making_queue(url,"dir.lst")
