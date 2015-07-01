#! /usr/bin/env python

import socket

HOST = '127.0.0.1'      # Symbolic name meaning the local host
PORT = 12345            # Arbitrary non-privileged port

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()

print 'Connected by', addr

data = conn.recv(1024)

print data

#conn.send(data)

conn.close()