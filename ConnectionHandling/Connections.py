__author__ = 'Admin'

from socket import socket


class Connection:

    serverSocket = socket(socket.AF_INET, socket.SOCK_STREAM)
    HOST = "127.0.0.1"
    PORT = 12345
    BUFFER_SIZE = 1024

    __init__()

    def initialiseConnection(self):
        serverSocket = socket(socket.AF_INET, socket.SOCK_STREAM)
        serverSocket.bind(HOST, PORT)
        serverSocket.listen(1)
        serverSocket.accept()

    def receiveMessage(self):
        return serverSocket.accept().recv()

    def closeConnection(self):
        serverSocket.close()