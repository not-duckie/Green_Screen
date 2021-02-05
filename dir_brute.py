#!/usr/bin/env python
import sys
import requests
from Queue import Queue
import threading
def making_queue():
    url = sys.argv[1]
    dic = sys.argv[2]
    q = Queue()
    f = open(dic,"rt")
    for i in f.readlines():
        q.put(i)
    while True:
        try:
            for i in range(5):
                worker = threading.Thread(target=brute, args=(url,q))
                worker.setDaemon(True)
                worker.start()
        except:
            print "done"
            exit()
    q.join()
def brute(url,q):
    i = q.get()
    url = url+i
    code = "500,200,401,403,301,302"
    r = requests.get(url)
    if str(r.status_code) in code:
        print url
    q.task_done()



making_queue()
