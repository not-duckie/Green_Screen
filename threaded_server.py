import threading
import socket
from Queue import Queue
def repy(q,k):
    data = "nice"
    client = q.get()
    print "connected to %s %d" %(k[0],k[1])
    while data :
        data = client.recv(1024)
        print "Client send : %s" %data
        print "replying back : %s" %data
        client.send(data)
    client.close()
    q.task_done()
    print "client closed connection to %s %d" %(k[0],k[1])

a = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
a.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
q = Queue()
a.bind(("127.0.0.1",8000))
a.listen(5)
print "listening..."
while True:
    client,(ip,port)=a.accept()
    q.put(client)
    worker = threading.Thread(target=repy,args=(q,(ip,port)))
    worker.setDaemon(True)
    worker.start()

