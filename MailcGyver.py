# -*- coding: utf-8 -*-
"""
MailcGyver - no shit
Created on Thu Nov  3 09:23:56 2016

@author: markus
"""

# python 3 libs
import socket, sys, _thread

# MailcGyver stuff
from IncommingThread import IncommingThread
from users import KNOWN

# localhost only on some high port
HOST = '127.0.0.1'
PORT = 2525

REPLY = dict(ready = "220 service ready\n".encode(), 
         ok = "250 OK\n".encode(), 
         start = "354: start mail input\n".encode(),
         close = "221: closing channel".encode())

# start socket
s = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
try:
    s.bind ((HOST, PORT))
except socket.error as msg:
    print ("socket failure: " + str(msg[0]) + ' Message ' + msg[1])
    sys.exit ()
s.listen (10)


# main
while True:
    conn, addr = s.accept ()
    print ("Connected with " + addr[0] + ":" + str(addr[1]))
    
    _thread.start_new_thread (IncommingThread , (conn, REPLY, KNOWN))
    
s.close()