#!/usr/bin/env python

import pexpect
import sys

def browse(name):
    print "="*25
    print name
    cmd = 'cd {}'.format(name)
    id.sendline(cmd)
    id.expect('ftp')
    if "550 Failed to change directory" in id.before.split('\r\n')[1]:
        print "Not a directory UwU"
        return
    id.sendline('ls')
    id.expect('ftp')
    for i in id.before.split('\r\n')[3:-2]:
        print i
    id.sendline('cd ..')
    id.expect('ftp')
    exit

try:
    a = sys.argv[1]
except:
    print "python ftp_search.py [password]"
id = pexpect.spawn('ftp localhost')
id.expect('Name')
id.sendline('duckie')
id.expect('Password')
id.sendline(a)
id.expect('ftp')
id.sendline('ls')
id.expect('ftp')
for i in id.before.split('\r\n'):
    print i

id.sendline('nlist')
id.expect('ftp')
b = id.before.split('\r\n')[3:-2]
for i in b:
    browse(i)


