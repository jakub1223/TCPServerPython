__author__ = 'Admin'

import socket


def connection():
    HOST = '127.0.0.1'      # Symbolic name meaning the local host
    PORT = 12345

    connection_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connection_socket.bind((HOST, PORT))
    connection_socket.listen(1)
    conn, addr = connection_socket.accept()

    print('Connected by', addr)

    while 1:
        data = conn.recv(1024)
        if not data:
                break

    print(data)
    print(data.len())
    print(type(data))

    conn.close()